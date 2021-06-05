### how to read text from websites ###

import urllib.request

# try:
#     with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as f:
#         print(f.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e.reason)

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
my_string = f.readlines()
without_b = [line.decode('utf-8') for line in my_string]

string_not_list = ''.join(without_b[37:])

print(string_not_list)