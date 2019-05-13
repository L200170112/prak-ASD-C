import re

f = open('Indonesia.txt', 'r')
pola = r'di\s\w+'

string = re.findall(pola, f.read())
print ('keseluruhan')
print (string)