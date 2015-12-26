#!/usr/bin/python
"""
Realistic Password Generator v0.32
AKA: Phantom User Generator
AKA: PUG

Andrew Morris
andrew.morris[at]intrepidusgroup com
morr.drew[at]gmail com
March 20, 2013

UPDATE:
02/26/2014

I updated a few things, but this code is still godawful. I'll optimize the functions and "pythofy" this with some classes
soon. Email me if you have any questions.

CHANGELOG:

-v0.2
Added some support for symbols. This was basically done by defining two strings containing common and less common symbols.
I'll also add more functions to the script to contain symbol stuff. Whenever I figure out how to work with dictionaries I'll
integrate a l33t translator for certain passwords.
-v0.3
Modified output to be Windows CMD friendly for adding users
-v0.31
Added support for creating John/Ophcrack friendly LM/NTLM hash dumps to skip the whole domain process and just benchmark
hash cracking.
-v0.32
Updated the script to generate the hashes themselves into John/Ophcrack format to benchmark hash cracking (for E.F.)

"""
##############################################
# CHANGE THESE VARIABLES FOR YOUR OWN SYSTEM #
##############################################

firstNameFile = 'male-names.txt'
lastNameFile = 'last-names.txt'

shitty = ['welcome','changeme','12345','secret','qwerty','123456','aaaaaa','internet','asd123', 'root', 'admin']
commonSymbols = '!?@$&*+-' # I tried to do the symbols as a list, but Python didn't like that, so I defined the symbols in a string instead
uncommonSymbols = '%^()"/<>~`[]{}|_'

import sys
import random 
import string

try:
	import smbpasswd
except ImportError:
	print "[!] Error: pysmbpasswd module not found"
	print "[+] Download from here: https://code.google.com/p/py-smbpasswd/"
	print "[+] Or install with 'sudo easy_install smbpasswd"
	exit()

if len(sys.argv) < 3:
	print "[+] Usage: 	python "+sys.argv[0]+" <number> <wordlist> <optional arguments>"
	print "[+] Example:	python %s 50 word.lst" % sys.argv[0]
	print "[+] Arguments:	--ntlm 		Generate empty LM hashes, force NTLM"
  	sys.exit()

''' Some global variables here '''
number = sys.argv[1]
randomNumber = random.randint(0,100)

try:
	with open(sys.argv[2], 'r') as f:
		randomWords = [line.strip() for line in f]
except IOError:
	print "[!] Error: Wordlist file not found: %s" % sys.argv[2]
	exit()

try:
	with open(firstNameFile, 'r') as f:
		firstNames = [line.strip() for line in f]
except IOError:
	print "[!] Error: First names file not found: %s" % firstNameFile
	exit()

try:
	with open(lastNameFile, 'r') as f:
		lastNames = [line.strip() for line in f]
except IOError:
	print "[!] Error: Last names file not found: %s" % lastNameFile
	exit()

def pass_Username(user):
	password = user+"1"
	return password

def pass_Password():
	password = "password"+str(random.randint(1,9))
	return password

def pass_DictWord():
	password = random.choice(randomWords)+str(random.randint(1,99))
	return password

def pass_DictWord_Upper(): # I'll figure out a better way to do this later
	password = random.choice(randomWords)+str(random.randint(1,99))
	return password

# Let's get some real ass randomness up in here
def random_Password_ULDS(size=random.randint(5,12), chars=string.ascii_lowercase + string.ascii_uppercase + string.digits + commonSymbols): 
	return ''.join(random.choice(chars) for x in range(size))

def random_Password_ULD(size=random.randint(5,12), chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def random_Password_LD(size=random.randint(5,12), chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def random_ShittyWord():
	password = random.choice(shitty)
	return password

def blank_Password(): # Not really sure why I actually defined this function...
	password = ""
	return password

def pass_DictWord_DigitsFirst():
	password = str(random.randint(1,99))+random.choice(randomWords)
	return password

def generateHashNTLM(username):
	emptyLM = 'AAD3B435B51404EEAAD3B435B51404EE'
	if randomNumber <=3: # 3%
		password = pass_Username(username)
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=6: # 3%
		password = pass_Password()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=12: # 6%
		password = pass_DictWord_DigitsFirst()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=64: # 52%
		password = pass_DictWord()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=74: # 10%
		password = random_Password_ULD()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=80: # 6%
		password = random_ShittyWord()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=87: # 7%
		password = random_Password_LD()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=88: # 1%
		password = ""
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=89: # 1%
		password = "andrewmorris"
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=98: # 9%
		password = pass_DictWord_Upper()
		try: 
			print username+':'+str(random.randint(1000,2000))+'AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
		except AttributeError: # This is in case the word starts with something other than a letter
			print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)
	elif randomNumber <=100: # 2%
		password = random_Password_ULDS()
		print username+':'+str(random.randint(1000,2000))+':AAD3B435B51404EEAAD3B435B51404EE:%s:::' % smbpasswd.nthash(password)

def generateHashLM(username):
	if randomNumber <=3: # 3%
		password = pass_Username(username)
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=6: # 3%
		password = pass_Password()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=12: # 6%
		password = pass_DictWord_DigitsFirst()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=64: # 52%
		password = pass_DictWord()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=74: # 10%
		password = random_Password_ULD()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=80: # 6%
		password = random_ShittyWord()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=87: # 7%
		password = random_Password_LD()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=88: # 1%
		password = ""
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=89: # 1%
		password = "andrewmorris"
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=98: # 9%
		password = pass_DictWord_Upper()
		try: 
			print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
		except AttributeError: # This is in case the word starts with something other than a letter
			print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)
	elif randomNumber <=100: # 2%
		password = random_Password_ULDS()
		print username+':'+str(random.randint(1000,2000))+':'+'%s:%s:::' % smbpasswd.hash(password)

def generateUser(lastNames, firstNames):
	firstName = random.choice(firstNames)
	lastName = random.choice(lastNames)
	name = firstNames[0]+lastNames
	return name.upper()

def letsGetSomeHashesUpInThisBitch():
	if '--ntlm' in sys.argv:
		for i in range(0, int(number)):
			name = generateUser(random.choice(lastNames), random.choice(firstNames))
			generateHashNTLM(name)
	else:
		for i in range(0, int(number)):
			name = generateUser(random.choice(lastNames), random.choice(firstNames))
			generateHashLM(name)

try:
	letsGetSomeHashesUpInThisBitch()
except:
	print "[!] Error: Something broke. Sorry :("
	exit()





