from rotor import Rotor
from string import ascii_lowercase

class RotorMachine:

    def __init__(self):
        #self.slow_rotor_max = 26 * 26 #26 rotations of the second wheel, 26^2 of the first wheel
        #self.slow_rotor_counter = 0
        self.slow_rotor = Rotor(26*26,[
            (24, 21),
            (25, 3),
            (26, 15),
            (1, 1),
            (2, 19),
            (3, 10),
            (4, 14),
            (5, 26),
            (6, 20),
            (7, 8),
            (8, 16),
            (9, 7),
            (10, 22),
            (11, 4),
            (12, 11),
            (13, 5),
            (14, 17),
            (15, 9),
            (16, 12),
            (17, 23),
            (18, 18),
            (19, 2),
            (20, 25),
            (21, 6),
            (22, 24),
            (23, 13)
            ])

        #self.medium_rotor_max = 26
        #self.medium_rotor_counter = 0
        self.medium_rotor = Rotor(26,[
            (26, 20),
            (1, 1),
            (2, 6),
            (3, 4),
            (4, 15),
            (5, 3),
            (6, 14),
            (7, 12),
            (8, 23),
            (9, 5),
            (10, 16),
            (11, 2),
            (12, 22),
            (13, 19),
            (14, 11),
            (15, 18),
            (16, 25),
            (17, 24),
            (18, 13),
            (19, 7),
            (20, 10),
            (21, 8),
            (22, 21),
            (23, 9),
            (24, 26),
            (25, 17)
            ])

        #self.fast_rotor_max = 1
        #self.fast_rotor_counter = 0
        self.fast_rotor = Rotor(1,[
            (1, 8),
            (2, 18),
            (3, 26),
            (4, 17),
            (5, 20),
            (6, 22),
            (7, 10),
            (8, 3),
            (9, 13),
            (10, 11),
            (11, 4),
            (12, 23),
            (13, 5),
            (14, 24),
            (15, 9),
            (16, 12),
            (17, 25),
            (18, 16),
            (19, 19),
            (20, 6),
            (21, 15),
            (22, 21),
            (23, 2),
            (24, 7),
            (25, 1),
            (26, 14)
            ])

    def press(self, letter):
        #shift_rotors
        self.slow_rotor.accept_input()
        self.medium_rotor.accept_input()
        self.fast_rotor.accept_input()

        #convert the letter to the corresponding number in first wheel
        lowercase_letter = letter.lower()
        letter_index = ascii_lowercase.index(lowercase_letter)

        #take the number through the slow rotor
        left_num = self.slow_rotor.value_pairs[letter_index][0] #ex. A gets the first left value, B gets the second
        rotor2_index = self.slow_rotor.get_pair_index(left_num)
        #print("Rotor 1 end: ", rotor2_index)

        #take the number through the medium rotor
        left_num = self.medium_rotor.value_pairs[rotor2_index][0]
        rotor3_index = self.medium_rotor.get_pair_index(left_num)
        #print("Rotor 2 end: ", rotor3_index)

        #take the number through the fast rotor
        left_num = self.fast_rotor.value_pairs[rotor3_index][0]
        final_index = self.fast_rotor.get_pair_index(left_num)
        #print("Left num:", left_num)
        #print("Rotor 3 end: ", final_index)

        #convert the index to a number
        final_letter = ascii_lowercase[final_index]

        return final_letter
        

    def shift_rotors(self):
        self.slow_rotor_max()
        pass

    def shift_rotor(self, distance_to_shift):
        pass
        

if __name__ == "__main__":
    rotors = RotorMachine()
    #print(rotors.press('a')) #expected e
    #print(rotors.press('b')) #expected q
    #print(rotors.press('c')) #expected t
    """
    print(rotors.press('a'))
    print(rotors.press('a')) #expected letter index 19 t
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    print(rotors.press('a'))
    """
    print(rotors.slow_rotor.get_left_values())
