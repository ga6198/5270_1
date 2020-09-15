#!C:/Program Files (x86)/Microsoft Visual Studio/Shared/Python37_64/python.exe

import cgi, cgitb
import sys
import string
#from ..CSC5270_HW1 import encrypt
#import encrypt
#from decrypt import decrypt

def getLetterFromIndex(letter):
    # _ is highest index at 26
    if letter == "_":
        return 26
    else:
        return string.ascii_lowercase.index(letter)

def getIndexFromLetter(index):
    if index == 26:
        return "_"
    else:
        return string.ascii_lowercase[index]

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

cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("encode_text") and form.getvalue("encode_key"):
    key = form.getvalue("encode_key")
    text = form.getvalue("encode_text")
    encrypted_string = encrypt(text, key)
    print("<h2>Encrypted String: %s</h2>" % encrypted_string)

"""
print("Content-Type: text/html\r\n")
print("<html>")
print("<head>")
print("<title>Vigenere Encoder/Decoder</title>")
print("</head>")

print("<body>")
print("<h1>Vigenere Encode</h1>")

#encryption box
print("<div class='box'>")
print("<form action = 'main.py' method = 'post'>")
print("Key: <input type='text' name='encode_key'><br />")
print("Text: <input type='text' name='encode_text'><br />")
print("<input type='submit' value='submit'/>")

#print("%s" % sys.version)
#print("%s" % sys.prefix)
print("</div>")

print("</body>")
print("</html>")
"""
