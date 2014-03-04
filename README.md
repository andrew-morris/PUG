PUG
===

#Phantom User Generator

## Disclaimer

I'm a horrible programmer. Don't judge me.

## Summary

This is a stupid script I wrote to generate 'realistic' passwords based on what I've seen
when cracking passwords on real compromised domain controllers. Obviously this can vary 
based on numerous factors including password policy. This is going to be used
in conjuction with my Person Generator script to populate users onto my test domain with
somewhat realistic passwords.

This version of the script accepts three parameters- number of hashes, wordlist, and arguments. I've
included a basic wordlist file that is actually a trimmed down common password list, which
happens to double as a list of very basic words. The username is used in the event that the
script hits the one percent and populates a user's password as the same thing as their username.

Feel free to modify the integer ranges as you feel necessary. There is no statistical analysis
behind these numbers. They literally came off the top of my head.

Again, this is a very basic script and I plan on improving it with additional features. 
Feel free to distribute or modify, I only ask that you give credit where credit is due.

Be well,

-Andrew

## Usage

```
python pug.py <number> <wordlist> <optional arguments>
  --ntlm 		Generate empty LM hashes, force NTLM
```

## Examples

Generate LM hashes
```
$ ./pug.py 5 word.lst
UCALLAHAN:1090:BE5570954C57AF1336077A718CCDF409:A5E031DE37E040DC730E19C50F52829F:::
CFROST:1728:498D61EB48C63ABCFF17365FAF1FFE89:F08B1E52BE814AB0BBEB2F64A85BE1AD:::
OLE:1524:41FED47DA31EC3AFC4045D3CFB2204EA:6023E744DD0D9F3599AA12DBBDD3FF5C:::
JDUFFY:1280:C0C4EF8E6ECC0092736F8EF8AD5EFB7A:FD24A64F195D97A90B05076C4865D79E:::
CJOHNS:1108:52B8CEC4E012F6301D71060D896B7A46:57950094A91EA1ADA8E17FDAD4759C2F:::
```
Generate NTLM hashes
```
$ python pug.py 5 word.lst --ntlm
CLYNCH:1956:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::
CHARVEY:1864:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::
CSTEWART:1290:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::
CFREDERICK:1591:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::
BHURLEY:1923:AAD3B435B51404EEAAD3B435B51404EE:31D6CFE0D16AE931B73C59D7E0C089C0:::
```
