# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/10/26 8:52 PM
# File      : MultiSelectedTreeview.py
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
        self.root.geometry("500x400+500+250")
        self.interface(file)


    def interface(self, file):
        """"界面编写位置"""
        label1 = tk.Label(self.root, text='Select')
        label1.place(relx=0.05, rely=0.02, relheight=0.4)
        # vertical scrollbar
        '''
            y_scrollbar.relx > treeview.relx
            y_scrollbar.rely = treeview.rely
            y_scrollbar.relh = treeview.relh
        '''
        y_scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        y_scrollbar.place(relx=0.82, rely=0.08, relwidth=0.01, relheight=0.3)
        self.tv = tk.ttk.Treeview(self.root, height=10, show='tree', selectmode=tk.EXTENDED, yscrollcommand=y_scrollbar.set)
        self.tv.place(relx=0.2, rely=0.08, width=300, relh=0.3)
        self.tv.bind("<<TreeviewSelect>>", self.item_select)

        self.info = pd.read_excel(file, sheet_name='Sheet1')
        states = list(self.info['State'].unique())
        self.cities = list(self.info['City'].unique())
        for state in states:
            st = self.tv.insert("", states.index(state), text=state)
            countries = list(self.info.loc[self.info.State == state, 'Country'].unique())
            for country in countries:
                cn = self.tv.insert(st, countries.index(country), text=country)
                cities = list(self.info.loc[(self.info.State == state) & (self.info.Country == country), 'City'].unique())
                for city in cities:
                    if type(city) is str:
                        self.tv.insert(cn, cities.index(city), text=city)
        y_scrollbar['command'] = self.tv.yview


        label2 = tk.Label(self.root, text='Confirm')
        label2.place(relx=0.05, rely=0.45, relheight=0.4)
        y_scrollbar_table = tk.Scrollbar(self.root, orient=tk.VERTICAL)
        y_scrollbar_table.place(relx=0.82, rely=0.45, relwidth=0.01, relheight=0.4)
        self.table = tk.ttk.Treeview(self.root, show='headings', columns=['0', '1', '2'], yscrollcommand=y_scrollbar_table.set, selectmode=tk.EXTENDED)
        self.table.bind("<<TreeviewSelect>>", self.item_select)
        self.table.heading(0, text='State', command=lambda: self.head_onclick('State'))
        self.table.heading(1, text='Country', command=lambda: self.head_onclick('Country'))
        self.table.heading(2, text='City', command=lambda: self.head_onclick('City'))
        self.table.column(0, anchor='center', width=20)
        self.table.column(1, anchor='center', width=20)
        self.table.column(2, anchor='center', width=20)
        self.table.place(relx=0.2, rely=0.45, width=300, relheight=0.4)
        y_scrollbar_table['command'] = self.table.yview
        self.table.bind("<<TreeviewSelect>>", self.select)


        self.entry = tk.Entry(self.root)
        self.entry.place(relx=0.2, rely=0.88, width=300, relheight=0.1)


    def item_select(self, event):
        selected = [self.tv.item(sel, 'text') for sel in self.tv.selection() if self.tv.item(sel, 'text') in self.cities]
        self.table.delete(*self.table.get_children())
        for sel in selected:
            state = ''.join(self.info.loc[self.info.City == sel, 'State'].unique())
            country = ''.join(self.info.loc[self.info.City == sel, 'Country'].unique())
            self.table.insert("", "end", values=(state, country, sel))

    def head_onclick(self, type):
        print(type)

    def select(self, event):
        self.entry.delete(0, "end")
        content = [self.table.item(select, "values") for select in self.table.selection()]
        self.entry.insert(INSERT, content)


if __name__ == '__main__':
    gui = GUI(file='geography_info.xlsx')
    gui.root.mainloop()