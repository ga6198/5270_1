from mappings import *

def applyCaesarCipher(plaintext_letter, key_letter):
    #skip space
    if plaintext_letter == " ":
        return " "

    plaintext = getLetterFromIndex(plaintext_letter)
    key = getLetterFromIndex(key_letter)
    encryption = (plaintext + key) % 27
    encryption_letter = getIndexFromLetter(encryption)
    return encryption_letter

def encrypt(stringToEncrypt, key):
    lowercaseString = stringToEncrypt.lower()
    lowercaseKey = key.lower()

    result = ""
    currentKeyIndex = 0 #holds the index of the key letter currently being used

    string_parts = lowercaseString.split() #remove spaces
    new_string_parts = [] #will hold the encrypted string parts
    
    for part in string_parts:
        new_string_part = ""
        for i in range(len(part)):
            current_letter = part[i]
            current_key_letter = lowercaseKey[currentKeyIndex]
            new_letter = applyCaesarCipher(current_letter, current_key_letter)

            #encrypt the current letter to the new letter
            #part[i] = new_letter
            new_string_part += new_letter

            #adjust the new key index
            currentKeyIndex += 1
            if currentKeyIndex >= len(lowercaseKey):
                currentKeyIndex = 0

        new_string_parts.append(new_string_part)

    #join all parts of the string back together with space
    encrypted_string = " ".join(new_string_parts)
    return encrypted_string
        
"""
print(applyCaesarCipher('a', '_')) #should be _
print(applyCaesarCipher('r', 'k')) #should be A
print(applyCaesarCipher('i', 'm')) #should be u
print(applyCaesarCipher('z', 'o')) #should be m
print(applyCaesarCipher('h', '_')) #should be G
"""

if __name__ == "__main__":
    stringToEncrypt = "Simplestring_"
    key = "asdf" #expected result: s_pulw vyr_ql_

    print(encrypt(stringToEncrypt, key))
