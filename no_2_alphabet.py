
alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

alpha_list = alphabet.split(',')

string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url_string = 'map'

def translate(string):
    translated = []

    words = string.split() #get separate words form string

    for word in words:
        new_word=''
        
        for letter in word:
            if letter.isalpha():
                for i in range(0,26): #max index is 25
                    if alpha_list[i] == letter: #check index of the letter
                        if i<=23:
                            new_word += alpha_list[i+2] #translate the letter
                        else:
                            new_word += alpha_list[i-24] #for last 2 indexes take letter from the begining (24-->0, 25-->1)
            else:
                new_word += letter

        #when letters in word are finished we add a finished word to the list
        translated.append(new_word)

    ready_text=' '.join(translated)

    return ready_text

print(translate(url_string))

# in url i added ocr (translated map)