from mappings import *

def applyCaesarDecrypt(plaintext_letter, key_letter):
    #skip space
    if plaintext_letter == " ":
        return " "

    plaintext = getLetterFromIndex(plaintext_letter)
    key = getLetterFromIndex(key_letter)
    decryption = (plaintext - key) % 27
    decryption_letter = getIndexFromLetter(decryption)
    return decryption_letter

def decrypt(stringToDecrypt, key):
    lowercaseString = stringToDecrypt.lower()
    lowercaseKey = key.lower()

    result = ""
    currentKeyIndex = 0 #holds the index of the key letter currently being used

    string_parts = lowercaseString.split() #remove spaces
    new_string_parts = [] #will hold the decrypted string parts
    
    for part in string_parts:
        new_string_part = ""
        for i in range(len(part)):
            current_letter = part[i]
            current_key_letter = lowercaseKey[currentKeyIndex]
            new_letter = applyCaesarDecrypt(current_letter, current_key_letter)

            #decrypt the current letter to the new letter
            #part[i] = new_letter
            new_string_part += new_letter

            #adjust the new key index
            currentKeyIndex += 1
            if currentKeyIndex >= len(lowercaseKey):
                currentKeyIndex = 0

        new_string_parts.append(new_string_part)

    #join all parts of the string back together with space
    decrypted_string = " ".join(new_string_parts)
    return decrypted_string

"""        
print(applyCaesarDecrypt('s', 'a')) #should be s
print(applyCaesarDecrypt('_', 's')) #should be i
print(applyCaesarDecrypt('p', 'd')) #should be m
print(applyCaesarDecrypt('u', 'f')) #should be p
print(applyCaesarDecrypt('q', 'z')) #should be s
"""


stringToDecrypt = "s_pulw vyr_ql_" 
key = "asdf" #expected result: s_pulw vyr_ql_

print(decrypt(stringToDecrypt, key))
