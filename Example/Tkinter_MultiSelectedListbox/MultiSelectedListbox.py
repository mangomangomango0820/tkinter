# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/10/23 10:44 PM
# File      : MultiSelectedListbox.py.py
# Tool      : PyCharm


import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import pandas as pd

class GUI:

    def __init__(self, file):
        self.root = tk.Tk()
        self.root.title('Title')
        self.root.geometry("600x500+500+250")
        self.interface(file)


    def interface(self, file):
        """"界面编写位置"""
        # horizontal scrollbar
        '''
            x_scrollbar.relx = listbox.relx
            x_scrollbar.rely > listbox.rely
            x_scrollbar.relw = listbox.relw
        '''
        x_scrollbar = tk.Scrollbar(self.root, orient=tk.HORIZONTAL)
        x_scrollbar.place(relx=0.2, rely=0.35, relwidth=0.5, relheight=0.015)


        # vertical scrollbar
        '''
            y_scrollbar.relx > listbox.relx
            y_scrollbar.rely = listbox.rely
            y_scrollbar.relh = listbox.relh
        '''
        y_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        y_scrollbar.place(relx=0.72, rely=0.03, relwidth=0.015, relheight=0.3)


        # create listbox
        label = tk.Label(self.root, text='Select Country')
        label.grid(row=8, column=1, padx=12, pady=80)
        info = pd.read_excel(file, sheet_name='Sheet1', na_values=True)
        cities = info.loc[info.State == "Asia Pacific", 'Country'].value_counts()
        citylist = list(cities.index.values)
        font = ('Courier New', 16, 'bold')
        list_box = tk.Listbox(self.root, font=font, selectmode=tk.EXTENDED,
                              width=20, height=10, activestyle='dotbox',
                              xscrollcommand=x_scrollbar.set,
                              yscrollcommand=y_scrollbar.set)
        list_box.insert(tk.END, *citylist)
        list_box.place(relx=0.2, rely=0.03, relwidth=0.5, relheight=0.3)

        x_scrollbar['command'] = list_box.xview
        y_scrollbar['command'] = list_box.yview

if __name__ == '__main__':
    gui = GUI(file='geography_info.xlsx')
    gui.root.mainloop()