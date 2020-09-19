class Rotor:

    def __init__(self, rotation_timer, value_pairs):
        self.rotation_timer = rotation_timer
        self.time_left_to_rotation = rotation_timer
        
        #pass in list with tuples of left values and right values
        self.value_pairs = value_pairs

    #given a left number, get the right number
    #returns index of right number and its letter
    def get_pair_index(self, left_num):
        #search for the given number on the right side of the wheel
        for i, val in enumerate(self.value_pairs):
            if self.value_pairs[i][1] == left_num:
                right_index = i
                return right_index

    def accept_input(self):
        self.time_left_to_rotation -=1
        if self.time_left_to_rotation == 0:
            #shift and reset timer
            self.shift()
            self.time_left_to_rotation = self.rotation_timer

        self.print()
            
    #shift down one value
    def shift(self):
        self.value_pairs.insert(0, self.value_pairs.pop())

    def print(self):
        print("Time Left to Rotation:",self.time_left_to_rotation)
        print(self.value_pairs)

    def get_left_values(self):
        display_text = ""
        for pair in self.value_pairs:
            display_text = display_text + str(pair[0]) + "\n"

        return display_text

    def get_right_values(self):
        display_text = ""
        for pair in self.value_pairs:
            display_text = display_text + str(pair[1]) + "\n"

        return display_text
        
if __name__ == "__main__":
    rotor1 = Rotor(3, [(1, 3), (2, 4)])
    rotor1.print()
    #rotor1.shift()
    #rotor1.print()

    rotor1.accept_input()
    rotor1.print()
    rotor1.accept_input()
    rotor1.print()
    rotor1.accept_input()
    rotor1.print()
