import re
import urllib.request

f = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
my_string = f.readlines()
without_b = [line.decode('utf-8') for line in my_string] # decode(utf-8) gets rid of 'b' (bytes) at the begining of new line
string_not_list = ''.join(without_b[37:])

### function makes a dictionary of characters and their frequencies ###
def check_frequency(text):

    splitted = re.split('(.)', text) # parenthesis make characters stay, otherwise i would get a list like ['', '', '']
    characters_only = list(filter(lambda x: x!='', splitted)) # getting rid of empty ''

    frequency = {}
    for i in range(0, len(characters_only)):
        character = characters_only[i]
        if character in frequency.keys():
            frequency[character] += 1
        else:
            frequency[character] = 1
    # print(frequency)
    return frequency

### function extract keys with the lowest value form the dictionary ###
### user can choose number of characters ###
def find_rare_characters(frequency_dict, number_of_characters):

    sorted_values = sorted(frequency_dict.values())
    the_rarest_values = sorted_values[:number_of_characters] # how many of the smallest values
    the_rarest_keys = []
    # print(the_rarest_values)

    for item in frequency_dict.items():
        if item[1] in the_rarest_values:
            the_rarest_keys.append(item[0])

    return the_rarest_keys

my_freq = check_frequency(string_not_list)
print(find_rare_characters(my_freq, 8))

# result = equality

#oops! it won't be sorted D: bc I only check if the value is in the_rarest_values
#so characters are ordered as they are in the text
#but let's try with that first!
#ideas for later: 
# en = 0
# for i in range(0, len(the_rarest_values)):
#for item in frequency_dict.items():
#if the_rarest_values[i]==item[1] the_rarest_keys.append(item[0]) 
#BUT values can by eg 10, 10, 2, so for second 10 we need different key

