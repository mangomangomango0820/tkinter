#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021.10.10
# @Author  : Xueshan Zhang
# @File    : Tkinter_SimpleCalculator.py
'''
1. use tkinter to create root window;
2. create a simple calculator user interface;
'''

from tkinter import *

# 1. create a window named with 'title' via 'tkinter'
root = Tk()
root.title('Title')

# 2. add label, text
# create label (‘text' cannot be changed at user interface)
# and locate label with grid nr.0 row and nr.0 column
label1 = Label(root, text='first number:')
label1.grid(row=0, column=0)
# add text and locate text with grid nr.1 row and nr.0 column
text1 = Text(root, width=30, height=1)
text1.grid(row=1, column=0)

label2 = Label(root, text='second number:')
label2.grid(row=2, column=0)
text2 = Text(root, width=30, height=1)
text2.grid(row=3, column=0)

label3 = Label(root, text='sum result:')
label3.grid(row=4, column=0)
text3 = Text(root, width=30, heigh=1)
text3.grid(row=5, column=0)

# 3. define function: read user-defined value in text1 and text2,
# plus, and output result in text3
def calculate():
    a1 = int(text1.get('1.0', END))     # get text, 1.0 means the 1st row and 1st character;
    a2 = int(text2.get('1.0', END))     # 'int' convert text in string format into int
    a3 = a1 + a2
    # clear text reulst in a3
    text3.delete('1.0', END)            # delete text
    text3.insert(INSERT, a3)

# 4. add button (root window, pre-defined text and command 'calculate')
# and locate button with grid nr.6 row and nr.0 column
button1 = Button(root, text='click for result:', command=calculate)
button1.grid(row=6, column=0)

# 5. add mainloop function
mainloop()