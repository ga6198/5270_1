import operator
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def count_letter_frequency(text):
    frequency = {}
    text = text.lower()
    
    for letter in text:
        if letter.isalpha() or letter == "_":
            if letter in frequency.keys():
                #increase the number of times seen
                frequency[letter] += 1
            else:
                #add the first entry
                frequency[letter] = 1

    #sort the dict by keys
    return dict(sorted(frequency.items(), key=operator.itemgetter(0)))

def calculate_average_usage(frequency_dict):
    total_letters = 0
    for letter in frequency_dict:
        total_letters += frequency_dict[letter]

    usage_dict = {}

    #calculate usage
    for letter in frequency_dict:
        usage = round(frequency_dict[letter]/total_letters, 4)
        usage_dict[letter] = usage

    return usage_dict

def display_bar_chart(frequency_dict):
    keys = frequency_dict.keys()
    y_pos = np.arange(len(keys))
    values = frequency_dict.values()

    plt.bar(y_pos, values, align='center', alpha=0.5)
    plt.xticks(y_pos, keys)
    plt.ylabel('Frequency')
    plt.title('Letter Usage')

    plt.show()

with open("cipher.txt") as f:
    text = f.read()

KEY_LENGTH = 4

for key_index in range(KEY_LENGTH):
    current_letters = ""

    text_with_offset = text[key_index:]

    print(text_with_offset)

    #get every fourth letter
    #initial offset is 0, then it is 1, then 2, up to key length
    for index, letter in enumerate(text_with_offset):
        if index % KEY_LENGTH == 0:
            current_letters += letter
    
    frequency = count_letter_frequency(current_letters)
    print("Letter Count for key index %d:" % key_index)
    print(frequency)

    usage = calculate_average_usage(frequency)
    print("Usage for key index %d" % key_index)
    print(usage)

    display_bar_chart(frequency)
        
    
print("Total Letter Counts For Entire Text:")
frequency = count_letter_frequency(text)
print(frequency)

#for key in sorted(frequency.keys()):
#    print("%s: %s" % (key, frequency[key]))

