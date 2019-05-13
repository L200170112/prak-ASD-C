import re

f = open('Indonesia.txt', 'r')
pola = r'di\w+'

string = re.findall(pola, f.read())
print ('keseluruhan')
print (string)