import itertools
from decrypt import *

def generateKeys():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']

    permutations = list(itertools.permutations(alphabet, 4))

    #print(permutations)

    for permutation in permutations:
        current_key = ''.join(permutation)
        f = open("keys.txt", "a")
        f.write(current_key + "\n")
        f.close()

    print("All possible keys written to keys.txt")

#statement to generate all possible keys
#generateKeys()

with open("cipher.txt") as f:
    ciphertext = f.read()


with open("keys.txt") as f:
    for line in f:
        key = line.strip()
        decryption = decrypt(ciphertext, key)
        #print(decryption)
        save_file = open("decryptions.txt", "a")
        save_file.write(key + " " + decryption + "\n")
        save_file.close()

    print("all combinations written to decryptions.txt")
