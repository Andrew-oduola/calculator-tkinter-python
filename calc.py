# Code with Drex

import tkinter as tk

class Calc(tk.Tk):
    def __init__(self):
        super().__init__()
        # Setting the window size and title
        self.geometry('280x410')
        self.title('Calculator')
        self.layout()

    # Define the layout of the calculator
    def layout(self):
        BTN_HEIGHT = 2
        BTN_WIDTH = 5
        BTN_FONT = ('Time', 12)

        # Main frame to the text label and the button frames
        self.main_frame = tk.Frame(self)
        self.main_frame.pack()

        # Frame to hold the display label
        self.text_frame = tk.Frame(self.main_frame)
        self.text_frame.grid(row=0, column=0)

        # Frame to hold the buttons
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.grid(row=1, column=0, pady=10)

        # Display label for showing the input and results
        self.text_label = tk.Label(self.text_frame, bg='black', anchor='e', fg='brown', height=2, width=23, font=('Arial', 16))
        self.text_label.grid(row=0, column=0, sticky=tk.E)

        # Display label for showing current input
        self.text_label2 = tk.Label(self.text_frame, bg='black', anchor='e', fg='white', height=2, width=23, font=('Arial', 16))
        self.text_label2.grid(row=1, column=0, sticky=tk.E)

        # Add buttons to the button frame
        # Each button calls a method when clicked
        self.ac_btn = tk.Button(self.button_frame, text='AC', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=self.clear)
        self.ac_btn.grid(row=0, column=0, padx=(10, 10))

        self.c_btn = tk.Button(self.button_frame, text='C', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=self.clean)
        self.c_btn.grid(row=0, column=1, padx=(0, 10))

        self.mod_btn = tk.Button(self.button_frame, text='%', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('%'))
        self.mod_btn.grid(row=0, column=2, padx=(0, 10))

        self.div_btn = tk.Button(self.button_frame, text='/', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('/'))
        self.div_btn.grid(row=0, column=3, padx=(0, 10))

        # Row of number buttons (7, 8, 9) and the multiplication button
        self.btn_7 = tk.Button(self.button_frame, text='7', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('7'))
        self.btn_7.grid(row=1, column=0, padx=(10, 10), pady=10)

        self.btn_8 = tk.Button(self.button_frame, text='8', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('8'))
        self.btn_8.grid(row=1, column=1, padx=(0, 10), pady=10)

        self.btn_9 = tk.Button(self.button_frame, text='9', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('9'))
        self.btn_9.grid(row=1, column=2, padx=(0, 10), pady=10)

        self.mul_btn = tk.Button(self.button_frame, text='*', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('*'))
        self.mul_btn.grid(row=1, column=3, padx=(0, 10), pady=10)

        # Row of number buttons (4, 5, 6) and the subtraction button
        self.btn_4 = tk.Button(self.button_frame, text='4', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('4'))
        self.btn_4.grid(row=2, column=0, padx=(10, 10))

        self.btn_5 = tk.Button(self.button_frame, text='5', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('5'))
        self.btn_5.grid(row=2, column=1, padx=(0, 10))

        self.btn_6 = tk.Button(self.button_frame, text='6', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('6'))
        self.btn_6.grid(row=2, column=2, padx=(0, 10))

        self.sub_btn = tk.Button(self.button_frame, text='-', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('-'))
        self.sub_btn.grid(row=2, column=3, padx=(0, 10))

        # Row of number buttons (1, 2, 3) and the addition button
        self.btn_1 = tk.Button(self.button_frame, text='1', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('1'))
        self.btn_1.grid(row=3, column=0, padx=(10, 10), pady=10)

        self.btn_2 = tk.Button(self.button_frame, text='2', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('2'))
        self.btn_2.grid(row=3, column=1, padx=(0, 10), pady=10)

        self.btn_3 = tk.Button(self.button_frame, text='3', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('3'))
        self.btn_3.grid(row=3, column=2, padx=(0, 10), pady=10)

        self.add_btn = tk.Button(self.button_frame, text='+', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('+'))
        self.add_btn.grid(row=3, column=3, padx=(0, 10), pady=10)

        # Row with 0 button, decimal button and equals button
        self.btn_0 = tk.Button(self.button_frame, text='0', font=BTN_FONT, height=BTN_HEIGHT, width=13, command=lambda: self.dig('0'))
        self.btn_0.grid(row=4, column=0, columnspan=2, padx=(10, 10))

        self.btn_ = tk.Button(self.button_frame, text='.', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=lambda: self.dig('.'))
        self.btn_.grid(row=4, column=2, padx=(0, 10))

        self.equal_btn = tk.Button(self.button_frame, text='=', font=BTN_FONT, height=BTN_HEIGHT, width=BTN_WIDTH, command=self.calculate)
        self.equal_btn.grid(row=4, column=3, padx=(0, 10))

    def dig(self, digit):
        self.digit = digit
        self.text_label2['text'] += self.digit

    def clear(self):
        self.text_label2['text'] = ''
        self.text_label['text'] = ''

    def clean(self):
        text = self.text_label2['text']
        cleaned_text = text[0:-1]
        self.text_label2['text'] = cleaned_text

    def calculate(self):
        try:
            self.result = eval(self.text_label2['text'])
            self.text_label['text'] = self.text_label2['text']
            self.text_label2['text'] = str(self.result)
        except:
            print('Error')



Calc().mainloop()