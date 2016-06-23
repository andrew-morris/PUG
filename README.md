PUG
===

#Phantom User Generator

## Summary

This is a stupid script I wrote to generate 'realistic' passwords based on what I've seen
when cracking passwords on real compromised domain controllers. Obviously this can vary 
based on numerous factors including password policy. This is going to be used
in conjuction with my Person Generator script to populate users onto my test domain with
somewhat realistic passwords.

Feel free to modify the integer ranges as you feel necessary. There is no statistical analysis
behind these numbers. They literally came off the top of my head.

Again, this is a very basic script and I plan on improving it with additional features. 
Feel free to distribute or modify.

## Usage

```
usage: pug.py [-h] [--hashes] [--ntlm] [--lm] [--count COUNT]
              [--first FIRSTNAMEFILE] [--last LASTNAMEFILE]
              [--wordlist WORDLISTFILE] [--cmd] [--cmd-domain]

optional arguments:
  -h, --help            show this help message and exit
  --hashes              output password hashes in pwdump format
  --ntlm                include NTLM password hashes
  --lm                  include deprecated LM hashes
  --count COUNT         amount of items to generate
  --first FIRSTNAMEFILE
                        file where first names are stored, default is data
                        /male-names.txt
  --last LASTNAMEFILE   file where last names are stored, default is data
                        /last-names.txt
  --wordlist WORDLISTFILE
                        seed file for passwords to be generated from, default
                        is data/word.lst
  --cmd                 output username and password in 'net user jsmith
                        password /add' format for use on Windows
  --cmd-domain          output username and password in 'net user jsmith
                        password /add /domain' format for use on Windows AD
```

## Examples

Generate ten random usernames and passwords
```
$ python pug.py --count 10
[+] kalford	Hammer44
[+] froberson	Bonzo93
[+] dwolfe	pickle38
[+] cwaters	7u5kp7
[+] scaldwell	root
[+] lfernandez	scotty4
[+] fmarsh	10f3H?aTxr
[+] sguerra	charity86
[+] iroth	sandi78
[+] patkins	suzuki81
```
Generate ten random usernames and NTLM password hashes in John the Ripper format
```
$ python pug.py --count 10 --hashes --ntlm
bbowen:1603:AAD3B435B51404EEAAD3B435B51404EE:42D04D8049AE53DBE0BFB359BFF6257D:::
canthony:1890A4E9FABE42E1985B7035D18B529E0ED8:AAD3B435B51404EEAAD3B435B51404EE:::
amosley:1894859A3049DAD0D10D78EA986D4E3ED8CA:AAD3B435B51404EEAAD3B435B51404EE:::
zmosley:1351:AAD3B435B51404EEAAD3B435B51404EE:32ED87BDB5FDC5E9CBA88547376818D4:::
mdean:1532:AAD3B435B51404EEAAD3B435B51404EE:13A991DB38E764976B669C44E98922FD:::
gclemons:1007:AAD3B435B51404EEAAD3B435B51404EE:1FBA69803F6D7A8AEDDB25308EEB6676:::
nfleming:1156:AAD3B435B51404EEAAD3B435B51404EE:2C12E60C994F3112F2EBC256C1D132B1:::
jaustin:1599CE37CCA4F3B086EAC11627F33E17DBBD:AAD3B435B51404EEAAD3B435B51404EE:::
jyoung:1448:AAD3B435B51404EEAAD3B435B51404EE:8E9EA18044D0C59FF9B1484E2B612363:::
lkeller:1264:AAD3B435B51404EEAAD3B435B51404EE:BF6EF7A24C198A69B177CCA583DF8671:::
```
Generate ten random usernames and LM (Legacy Windows LanManager) password hashes in John the Ripper format
```
$ python pug.py --count 10 --hashes --lm
mquinn:1069:A30512FDA396A13D1BC0FF9C535C9968:C73B0D30ED8E9150CA29138C04F45D34:::
klowe:1655:EE6C0CEE1192C24FC2265B23734E0DAC:254269D2099C3EB4FB1D99F599890B51:::
ebullock:1153:801DFE004BE9E2B9FF17365FAF1FFE89:74F017B8E34FEFB6478A074EBA256264:::
anielsen:1394:C895EA6D3920068D9C5014AE4718A7EE:8970E2C3AACFC7E3D738C1BDF15AB152:::
xpugh:1899:87171EED555DC3C11F66994B4FC2476E:68C993814C2473E336AE6982AE8DF47A:::
dfrancis:1177:6FFB7E3402723D8EAAD3B435B51404EE:99EC5205A7494239039915A344FE86EA:::
denglish:1844:8DB52C8848E2E84C25AD3B83FA6627C7:2DC579DDCF5EA456A8B66BDA7FD01120:::
efitzpatrick:1694:234668513F8AFB89AAD3B435B51404EE:A787D5F7543F878C8F2C21F101CBBD85:::
mcook:1456:7935889242C3A90A36077A718CCDF409:1F6BE2EFEA57D3D5C393927CED8A4135:::
zoneal:1710:1BE94EECF7D8AC9509752A3293831D17:6DF751F35CCEE7B55EAE90AFF17E339E:::
```
Generate ten random usernames and passwords in a format to be added to a local Windows system with the command prompt
```
$ python pug.py --count 10 --cmd
net user wroberts hunter2 /add
net user gmcdonald h1gnpz5x1h /add
net user cstrong 51tiffany /add
net user aolson rocky61 /add
net user thicks vicki27 /add
net user shunter shunter1 /add
net user sparsons spartan61 /add
net user kbest lions47 /add
net user arivas jasmin89 /add
net user apickett greg43 /add
```
Generate ten random usernames and passwords in a format to be added to a Windows Active Directory domain with the command prompt
```
$ python pug.py --count 10 --cmd-domain
net user mcastro beaches44 /add /domain
net user eglenn stars73 /add /domain
net user bmcknight eeyore37 /add /domain
net user jchandler  /add /domain
net user cwatts Bond00781 /add /domain
net user gholden westlife46 /add /domain
net user swong rc3r8thzcyj8 /add /domain
net user shyde 87start /add /domain
net user mmcbride password4 /add /domain
net user bfuentes secret /add /domain
```

