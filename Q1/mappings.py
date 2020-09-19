import string

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

