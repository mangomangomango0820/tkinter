# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/11/12 4:18 PM
# File      : a.py
# Tool      : PyCharm
# Purpose   : example 1, a.py

import tkinter as tk
import threading
from b import logic
#
# global flag, input, output

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('example')
        self.root.geometry("500x300+500+250")
        self.interface()
        self.flag = threading.Event()

    def interface(self):
        """"界面编写位置"""
        self.Button0 = tk.Button(self.root, text="start", command=self.start, bg="#7bbfea")
        self.Button0.place(x=50, y=15, width=70, height=30)
        self.Button1 = tk.Button(self.root, text="stop", command=self.stop, bg="#7bbfea")
        self.Button1.place(x=150, y=15, width=70, height=30)
        self.Button2 = tk.Button(self.root, text="continue", command=self.conti, bg="#7bbfea")
        self.Button2.place(x=250, y=15, width=70, height=30)
        self.Button3 = tk.Button(self.root, text="clear", command=self.clear, bg="#7bbfea")
        self.Button3.place(x=350, y=15, width=70, height=30)

        label = tk.Label(text='Input')
        label.place(x=50, y=70)
        self.entry00 = tk.StringVar()
        self.entry00.set("Please give a number here")
        self.entry0 = tk.Entry(self.root, textvariable=self.entry00)
        self.entry0.place(x=100, y=70, width=300, height=30)
        self.entry0.bind('<Button-1>',  self.delete)

        label = tk.Label(text='Output')
        label.place(x=50, y=180)
        self.w1 = tk.Text(self.root)
        self.w1.place(x=100, y=120, width=300, height=170)
        self.output = self.w1

    def seal(self):
        self.input = self.entry00.get()
        logic(self.flag, self.input, self.output).event()

    def clear(self):
        self.w1.delete('0.0', 'end')

    def start(self):
        '''
        set internal flag to True and start threading
        :return:
        '''
        self.flag.set()
        self.T = threading.Thread(target=self.seal)
        self.T.setDaemon(True)
        self.T.start()

    def stop(self):
        logic(self.flag, self.input, self.output).stop()

    def conti(self):
        logic(self.flag, self.input, self.output).conti()

    def delete(self, event):
        self.entry0.delete(0, tk.END)


if __name__ == '__main__':
    a = GUI()
    a.root.mainloop()