import urllib.request

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
my_string = f.readlines()
without_b = [line.decode('utf-8') for line in my_string] # decode(utf-8) gets rid of 'b' (bytes) at the begining of new line
string_not_list = ''.join(without_b[21:])

import re

print(re.findall('[A_Z]{3}[a-z][A-Z]{3}', string_not_list))