# _*_coding : UTF_8 _*_
# Author    : Xueshan Zhang
# Date      : 2022/10/8 10:41 AM
# File      : MultilevelCombobox.py
# Tool      : PyCharm

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from PIL import Image, ImageTk
import pickle
import json

image = None
im = None

class LogIn:
    def __init__(self, info):
        self.info = info
        self.un, self.pw = '', ''
        self.root = tk.Tk()
        self.root.title('Log in')
        self.root.geometry('450x300+500+250')
        self.interface()

    def interface(self):
        global image
        global im
        ### create canvas
        canvas = tk.Canvas(self.root, height=300, width=450)
        image = Image.open("background.png")
        im = ImageTk.PhotoImage(image)
        bg = canvas.create_image(0, 0, anchor='nw', image=im)
        canvas.pack(side='top')

        ### create labels and entries;
        tk.Label(self.root, text='Username').place(x=80, y=100)
        tk.Label(self.root, text='Password').place(x=80, y=150)
        #
        varUN = tk.StringVar()
        varUN.set('xxx@gmail.com')
        self.entryUN = tk.Entry(self.root, textvariable=varUN)
        self.entryUN.place(x=160, y=100)
        #
        varPW = tk.StringVar()
        self.entryPW = tk.Entry(self.root, textvariable=varPW, show='*')
        self.entryPW.place(x=160, y=150)

        btn_login = tk.Button(self.root, text='Log In', command=self.usr_login)
        btn_login.place(x=100, y=230)
        btn_exit = tk.Button(self.root, text='Exit', command=self.root.destroy)
        btn_exit.place(x=280, y=230)

    def usr_login(self):
        '''
        log in event bind to button Log in
        if pickle file exists, load it; else, generate it;
        :return:
        '''
        self.un = self.entryUN.get()
        self.pw = self.entryPW.get()
        try:
            with open('usrs_info.pickle', 'rb') as usr_file:
                usrs_info = pickle.load(usr_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as usr_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, usr_file)
        else:
            if self.un in usrs_info:
                if self.pw == usrs_info[self.un]:
                    tk.messagebox.showinfo(title='Welcome', message=f"'{self.un}' Log in successfully.")
                    geo = tk.Toplevel()
                    Geo(geo, self.info)
                    geo.transient(self.root)
                    geo.mainloop()
                else:
                    # tk.messagebox.showinfo(title='Error', message=f"Please retry with your password '{self.pw}'.")
                    is_retry = tk.messagebox.askyesno('Notice', f"Please retry with your password '{self.pw}' first.")
                    if not is_retry:
                        self.usr_forget()
            else:
                is_sign_up = tk.messagebox.askyesno('Notice', 'Please register your personal account first.')
                if is_sign_up:
                    self.usr_sign_up()

    def usr_sign_up(self):
        def sign():
            # get data
            np = newpw.get()
            npf = newpw_confirm.get()
            nn = newun.get()
            # judge if data has already been registered;
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
                if np != npf:
                    tk.messagebox.showerror(title='Error', message='Confirm Your Password !')
                elif nn in exist_usr_info:
                    tk.messagebox.showerror(title='Error', message='This username has been registered !')
                else:
                    exist_usr_info[nn] = np
                    with open('usrs_info.pickle', 'wb') as usr_file:
                        # write username and password in user_info_pickle file in the format of dict
                        pickle.dump(exist_usr_info, usr_file)
                    tk.messagebox.showinfo(title='Welcome', message=f"You register with '{nn}', '{np}' successfully.")
                # destory top level window
                win_signup.destroy()

        win_signup = tk.Toplevel(self.root)
        win_signup.title('Welcome to Register')
        win_signup.geometry('450x300+500+250')

        newun = tk.StringVar()
        newun.set(self.un)
        tk.Label(win_signup, text='Username').place(x=30, y=80)
        entry_newun = tk.Entry(win_signup, textvariable=newun)
        entry_newun.place(x=160, y=80)

        newpw = tk.StringVar()
        tk.Label(win_signup, text='Password').place(x=30, y=120)
        entry_newpw = tk.Entry(win_signup, textvariable=newpw, show='*')
        entry_newpw.place(x=160, y=120)
        newpw_confirm = tk.StringVar()
        tk.Label(win_signup, text='Confirm password').place(x=30, y=160)
        entry_newpw_confirm = tk.Entry(win_signup, textvariable=newpw_confirm, show='*')
        entry_newpw_confirm.place(x=160, y=160)

        btn_signup_confirm = tk.Button(win_signup, text='Sign Up', command=sign)
        btn_signup_confirm.place(x=200, y=220)

    def usr_forget(self):
        def forget():
            # get data
            np = newpw.get()
            nn = newun.get()
            # judge if data has already been registered;
            with open('usrs_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
                if nn in exist_usr_info:
                    newpw.set(exist_usr_info[nn])

        win_forget = tk.Toplevel(self.root)
        win_forget.title('Welcome to Find Your Password')
        win_forget.geometry('450x300+500+250')

        newun = tk.StringVar()
        newun.set(self.un)
        tk.Label(win_forget, text='Username').place(x=80, y=100)
        entry_newun = tk.Entry(win_forget, textvariable=newun)
        entry_newun.place(x=160, y=100)

        newpw = tk.StringVar()
        tk.Label(win_forget, text='Password').place(x=80, y=150)
        entry_newpw = tk.Entry(win_forget, textvariable=newpw)
        entry_newpw.place(x=160, y=150)

        btn_find = tk.Button(win_forget, text='Find', command=forget)
        btn_find.place(x=100, y=230)
        btn_find = tk.Button(win_forget, text='Exit', command=win_forget.destroy)
        btn_find.place(x=280, y=230)


class Geo:
    def __init__(self, root, info):
        self.info = info
        self.root = root
        self.root.title('Choose')
        self.root.geometry('500x450+500+250')
        self.interface()

    def interface(self):
        self.states = list(self.info.keys())
        lstate = tk.Label(self.root, text='State')
        lstate.grid(row=1, column=0, padx=20, pady=20)
        self.cbstate = Combobox(self.root, state='normal', values=self.states, width=30, postcommand=self.automatchstate)
        self.cbstate.grid(row=1, column=1, padx=20, pady=20)
        self.cbstate.bind('<<ComboboxSelected>>', self.stateslist)

        lcountry = tk.Label(self.root, text='Country')
        lcountry.grid(row=2, column=0, padx=20, pady=20)
        self.cbcountry = Combobox(self.root, state='normal', width=30, postcommand=self.automatchcountry)
        self.cbcountry.grid(row=2, column=1, padx=20, pady=20)
        self.cbcountry.bind('<<ComboboxSelected>>', self.countrieslist)

        lcity = tk.Label(self.root, text='City')
        lcity.grid(row=3, column=0, padx=20, pady=20)
        self.cbcity = Combobox(self.root, state='normal', width=30, postcommand=self.automatchcity)
        self.cbcity.grid(row=3, column=1, padx=20, pady=20)
        self.cbcity.bind('<<ComboboxSelected>>', self.citieslist)

        lval = tk.Label(self.root, text='Val')
        lval.grid(row=4, column=0, padx=20, pady=20)
        self.cbval = Combobox(self.root, state='normal', width=30)
        self.cbval.grid(row=4, column=1, padx=20, pady=20)
        self.cbval.bind('<<ComboboxSelected>>', self.valslist)

        btn_collect = tk.Button(self.root, text='Collect', command=self.table)
        btn_collect.place(relx=0.15, rely=0.6, width=70, height=30)
        btn_clear = tk.Button(self.root, text='Clear', command=self.clear)
        btn_clear.place(relx=0.4, rely=0.6, width=70, height=30)
        btn_exit = tk.Button(self.root, text='Exit', command=self.root.destroy)
        btn_exit.place(relx=0.65, rely=0.6, width=70, height=30)

    def clear(self):
        self.cbstate.set('')
        self.cbcountry.set('')
        self.cbcity.set('')
        self.cbval.set('')
        self.tree.delete(*self.tree.get_children())

    def table(self):
        def item_select(event):
            for select in self.tree.selection():
                print(self.tree.item(select, "values"))
        def head_onclick(type):
            print(type)

        self.tree = tk.ttk.Treeview(self.root, show='headings', columns=['0', '1'])
        self.tree.heading(0, text='item', command=lambda: head_onclick('item'))
        self.tree.heading(1, text='value', command=lambda: head_onclick('value'))
        self.tree.column(0, anchor='center')
        self.tree.column(1, anchor='center')

        self.tree.insert("", "end", values=('state', self.cbstate.get()))
        self.tree.insert("", "end", values=("country", self.cbcountry.get()))
        self.tree.insert("", "end", values=("city", self.cbcity.get()))
        self.tree.insert("", "end", values=("val", self.cbval.get()))
        self.tree.place(relx=0.1, rely=0.7, width=400, height=100)
        self.tree.bind("<<TreeviewSelect>>", item_select)

    def stateslist(self, event):
        self.cbstate['values'] = [i for i in self.states if self.cbstate.get() in i]
        self.cbcountry['values'] = list(self.info.get(self.cbstate.get()).keys())

    def countrieslist(self, event):
        self.cbcountry['values'] = list(self.info.get(self.cbstate.get()).keys())
        self.cbcity['values'] = list(self.info.get(self.cbstate.get()).get(self.cbcountry.get()).keys())

    def citieslist(self, event):
        self.cbcity['values'] = list(self.info.get(self.cbstate.get()).get(self.cbcountry.get()).keys())
        self.cbval['values'] = self.info.get(self.cbstate.get()).get(self.cbcountry.get()).get(self.cbcity.get())

    def valslist(self, event):
        self.cbval['values'] = list(self.info.get(self.cbstate.get()).get(self.cbcountry.get()).get(self.cbcity.get()))

    def automatchstate(self):
        self.cbstate['values'] = [i for i in self.cbstate['values'] if self.cbstate.get() in i]

    def automatchcountry(self):
        self.cbcountry['values'] = [i for i in self.cbcountry['values'] if self.cbcountry.get() in i]

    def automatchcity(self):
        self.cbcity['values'] = [i for i in self.cbcity['values'] if self.cbcity.get() in i]

if __name__ == '__main__':
    f = open("geography_info.json")
    geo_info = json.load(f)
    f.close()

    exLogIn = LogIn(geo_info)
    exLogIn.root.mainloop()