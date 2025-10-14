import tkinter as tk

equation_label = ""

class Calculator:
    def __init__(self, root):

        global equation_label
        self.equation_label = equation_label

        self.root = root
        self.root.resizable(False,False)
        self.root.title("Calculator")

        self.label = tk.Label(root,textvariable=equation_label,font=('consolas',20), bg="white", width=24, height=2)
        self.label.pack()

        self.frame = tk.Frame(root)
        self.frame.pack()

        self.buttons(self.frame)

        self.frame.bind("<Key>",self.key_event)
        self.frame.focus_set()

    def buttons(self,frame):
        button1 = tk.Button(frame, text=1, height=4, width=9, font=35,
                         command=lambda:self.button_press(1))
        button1.grid(row=0, column=0 )

        button2 = tk.Button(frame, text=2, height=4, width=9, font=35,
                         command=lambda:self.button_press(2))
        button2.grid(row=0, column=1 )

        button3 = tk.Button(frame, text=3, height=4, width=9, font=35,
                         command=lambda:self.button_press(3))
        button3.grid(row=0, column=2 )

        button4 = tk.Button(frame, text=4, height=4, width=9, font=35,
                         command=lambda:self.button_press(4))
        button4.grid(row=1, column=0 )

        button5 = tk.Button(frame, text=5, height=4, width=9, font=35,
                         command=lambda:self.button_press(5))
        button5.grid(row=1, column=1 )

        button6 = tk.Button(frame, text=6, height=4, width=9, font=35,
                         command=lambda:self.button_press(6))
        button6.grid(row=1, column=2 )

        button7 = tk.Button(frame, text=7, height=4, width=9, font=35,
                         command=lambda:self.button_press(7))
        button7.grid(row=2, column=0 )

        button8 = tk.Button(frame, text=8, height=4, width=9, font=35,
                         command=lambda:self.button_press(8))
        button8.grid(row=2, column=1 )

        button9 = tk.Button(frame, text=9, height=4, width=9, font=35,
                         command=lambda:self.button_press(9))
        button9.grid(row=2, column=2 )

        button0 = tk.Button(frame, text=0, height=4, width=9, font=35,
                         command=lambda:self.button_press(0))
        button0.grid(row=3, column=0 )

        plus = tk.Button(frame,text="+",height = 4,width = 9,font = 35,
                        command=lambda:self.button_press("+"))
        plus.grid(row = 0,column = 3)

        minus = tk.Button(frame,text="-",height = 4,width = 9,font = 35,
                        command=lambda:self.button_press("-"))
        minus.grid(row = 1,column = 3)

        multiply = tk.Button(frame,text="*",height = 4,width = 9,font = 35,
                        command=lambda:self.button_press("*"))
        multiply.grid(row = 2,column = 3)

        division = tk.Button(frame,text="/",height = 4,width = 9,font = 35,
                        command=lambda:self.button_press("/"))    
        division.grid(row = 3,column = 3)

        equal = tk.Button(frame,text="=",height = 4,width = 9,font = 35,
                        command=self.equals)
        equal.grid(row = 3,column = 2)

        clear = tk.Button(frame,text="C",height = 4,width = 9,font = 35,
                        command=self.clear) 
        clear.grid(row = 3,column = 1)

    def button_press(self, value):
        global equation_label
        equation_label = equation_label + str(value)
        self.label.config(text=equation_label)

    def equals(self):
        global equation_label
        try:
            total = str(eval(equation_label))
            self.label.config(text=total)
            equation_label = total
        except ZeroDivisionError:
            self.label.config(text="Arithmetic Error")
            equation_label = ""
        except SyntaxError:
            self.label.config(text="Syntax Error")
            equation_label = ""
        except Exception as e:
            self.label.config(text="Error")
            equation_label = ""

    def key_event(self, event):
        key = event.keysym
        if key in ('0','1','2','3','4','5','6','7','8','9'):
            self.button_press(key)
        elif key in ('plus','KP_Add'):
            self.button_press('+')
        elif key in ('minus','KP_Subtract'):
            self.button_press('-')
        elif key in ('asterisk','KP_Multiply'):
            self.button_press('*')
        elif key in ('slash','KP_Divide'):
            self.button_press('/')
        elif key in ('Return','KP_Enter','equal'):
            self.equals()
        elif key == ('BackSpace'):
            global equation_label
            equation_label = equation_label[:-1]
            self.label.config(text=equation_label)
        elif key == ('c','delete'):
            self.clear()
        else:
            pass
    def clear(self):
        global equation_label
        equation_label = ""
        self.label.config(text=equation_label)

if __name__=="__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()