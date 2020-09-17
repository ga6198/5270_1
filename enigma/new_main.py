import tkinter as tk
from rotormachine import *

class Window:
    
    def __init__(self, window):
        
        self.machine = RotorMachine()

        #left label
        self.left_label=tk.Label(window, text="A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ")
        self.left_label.place(x=25, y=50)

        #left rotor
        self.left_rotor=tk.Button(window, height=30, width=10)
        self.left_rotor.place(x=45, y=45)
        #self.left_rotor.bind("<Button-1>", self.shift_left_rotor)
        
        self.left_rotor_left=tk.Label(window, text=self.machine.slow_rotor.get_left_values())
        self.left_rotor_left.place(x=50, y=50)

        self.left_rotor_right=tk.Label(window, text=self.machine.slow_rotor.get_right_values())
        self.left_rotor_right.place(x=100, y=50)

        self.left_rotor_down = tk.Button(window, text="Shift Down")
        self.left_rotor_down.place(x=50, y=520)
        self.left_rotor_down.bind("<Button-1>", self.shift_left_rotor)

        #middle rotor
        self.middle_rotor=tk.Button(window, height=30, width=10)
        self.middle_rotor.place(x=150, y=45)

        self.middle_rotor_left=tk.Label(window, text=self.machine.medium_rotor.get_left_values())
        self.middle_rotor_left.place(x=155, y=50)

        self.middle_rotor_right=tk.Label(window, text=self.machine.medium_rotor.get_right_values())
        self.middle_rotor_right.place(x=205, y=50)

        self.middle_rotor_down = tk.Button(window, text="Shift Down")
        self.middle_rotor_down.place(x=155, y=520)
        self.middle_rotor_down.bind("<Button-1>", self.shift_middle_rotor)

        #right rotor
        self.right_rotor=tk.Button(window, height=30, width=10)
        self.right_rotor.place(x=250, y=45)

        self.right_rotor_left=tk.Label(window, text=self.machine.fast_rotor.get_left_values())
        self.right_rotor_left.place(x=255, y=50)

        self.right_rotor_right=tk.Label(window, text=self.machine.fast_rotor.get_right_values())
        self.right_rotor_right.place(x=305, y=50)

        self.right_rotor_down = tk.Button(window, text="Shift Down")
        self.right_rotor_down.place(x=255, y=520)
        self.right_rotor_down.bind("<Button-1>", self.shift_right_rotor)

        #right label
        self.right_label=tk.Label(window, text="A\nB\nC\nD\nE\nF\nG\nH\nI\nJ\nK\nL\nM\nN\nO\nP\nQ\nR\nS\nT\nU\nV\nW\nX\nY\nZ")
        self.right_label.place(x=330, y=50)

        #text space label
        self.textarea_label=tk.Label(window, text="Input")
        self.textarea_label.place(x=130, y=580)
        
        #enter text space
        self.textarea=tk.Entry()
        self.textarea.place(x=130, y=600)
        self.textarea.bind("a", lambda event, arg='a': self.encrypt(event, arg))
        self.textarea.bind("b", lambda event, arg='b': self.encrypt(event, arg))
        self.textarea.bind("c", lambda event, arg='c': self.encrypt(event, arg))
        self.textarea.bind("d", lambda event, arg='d': self.encrypt(event, arg))
        self.textarea.bind("e", lambda event, arg='e': self.encrypt(event, arg))
        self.textarea.bind("f", lambda event, arg='f': self.encrypt(event, arg))
        self.textarea.bind("g", lambda event, arg='g': self.encrypt(event, arg))
        self.textarea.bind("h", lambda event, arg='h': self.encrypt(event, arg))
        self.textarea.bind("i", lambda event, arg='i': self.encrypt(event, arg))
        self.textarea.bind("j", lambda event, arg='j': self.encrypt(event, arg))
        self.textarea.bind("k", lambda event, arg='k': self.encrypt(event, arg))
        self.textarea.bind("l", lambda event, arg='l': self.encrypt(event, arg))
        self.textarea.bind("m", lambda event, arg='m': self.encrypt(event, arg))
        self.textarea.bind("n", lambda event, arg='n': self.encrypt(event, arg))
        self.textarea.bind("o", lambda event, arg='o': self.encrypt(event, arg))
        self.textarea.bind("p", lambda event, arg='p': self.encrypt(event, arg))
        self.textarea.bind("q", lambda event, arg='q': self.encrypt(event, arg))
        self.textarea.bind("r", lambda event, arg='r': self.encrypt(event, arg))
        self.textarea.bind("s", lambda event, arg='s': self.encrypt(event, arg))
        self.textarea.bind("t", lambda event, arg='t': self.encrypt(event, arg))
        self.textarea.bind("u", lambda event, arg='u': self.encrypt(event, arg))
        self.textarea.bind("v", lambda event, arg='v': self.encrypt(event, arg))
        self.textarea.bind("w", lambda event, arg='w': self.encrypt(event, arg))
        self.textarea.bind("x", lambda event, arg='x': self.encrypt(event, arg))
        self.textarea.bind("y", lambda event, arg='y': self.encrypt(event, arg))
        self.textarea.bind("z", lambda event, arg='z': self.encrypt(event, arg))


        #output text space label
        self.textarea_label=tk.Label(window, text="Output")
        self.textarea_label.place(x=130, y=630)
        
        #output text space
        #self.outputarea_text = ""
        self.outputarea=tk.Entry() # tk.Entry(state='disabled')
        self.outputarea.place(x=130, y=650)

    def shift_left_rotor(self, event):
        self.machine.slow_rotor.shift()
        self.left_rotor_left['text'] = self.machine.slow_rotor.get_left_values()
        self.left_rotor_right['text'] = self.machine.slow_rotor.get_right_values()

    def shift_middle_rotor(self, event):
        self.machine.medium_rotor.shift()
        self.middle_rotor_left['text'] = self.machine.medium_rotor.get_left_values()
        self.middle_rotor_right['text'] = self.machine.medium_rotor.get_right_values()

    def shift_right_rotor(self, event):
        self.machine.fast_rotor.shift()
        self.right_rotor_left['text'] = self.machine.fast_rotor.get_left_values()
        self.right_rotor_right['text'] = self.machine.fast_rotor.get_right_values()

    def encrypt(self, event, arg):
        print(arg)
        encrypted_value = self.machine.press(arg)
        self._update_view()

        #self.outputarea_text += encrypted_value
        #len(self.outputarea['text'])
        self.outputarea.insert(tk.END, encrypted_value)

    def _update_view(self):
        self.left_rotor_left['text'] = self.machine.slow_rotor.get_left_values()
        self.left_rotor_right['text'] = self.machine.slow_rotor.get_right_values()

        self.middle_rotor_left['text'] = self.machine.medium_rotor.get_left_values()
        self.middle_rotor_right['text'] = self.machine.medium_rotor.get_right_values()

        self.right_rotor_left['text'] = self.machine.fast_rotor.get_left_values()
        self.right_rotor_right['text'] = self.machine.fast_rotor.get_right_values()



window = tk.Tk()

#machine = RotorMachine()

#lbl=tk.Label(window, text=machine.slow_rotor.get_left_values())
#lbl.place(x=50, y=50)

#lbl=tk.Label(window, text=machine.slow_rotor.get_right_values())
#lbl.place(x=100, y=50)



#txtfld=tk.Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=80, y=150)
mywin=Window(window)
window.title('3 Rotor')
window.geometry("375x720")
window.mainloop()
    
