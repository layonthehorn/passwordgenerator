#
# Name:        GUIPassword
# Purpose: A GUI based password generating program
#
# Author:      Layonthehorn
#
# Created:     30/12/2017
# Copyright:   (c) catma 2017
# Licence:     <your licence>
#


import string, webbrowser
from tkinter import *
from RandomPass import RandomValue, PassChecker



class App(PassChecker,object):
    # This is a GUI based password generator

    def __init__(self):

        self.cpofpass = ''
        #
        # print(self.cpofpass)
        #
        # defining the window as root
        self.root = Tk()

        # setting a default size for the window
        self.root.geometry('250x250')
        # setting the title for the window
        self.root.wm_title("Password Generator")
        # defining a label with the window root and some text
        self.label = Label (self.root, text= "Enter the length of your password.")
        # packing the label on to the window
        self.label.pack()

        # defining a var text to be filled later
        self.entrytext = StringVar()
        # defining a box for users to input data and then packing it to the window
        Entry(self.root, textvariable=self.entrytext).pack()
        # setting a var to hold the button text
        self.buttontext = StringVar()
        # setting the text as Generate
        self.buttontext.set("Generate")
        # building a button for users to click
        Button(self.root, textvariable=self.buttontext, command=lambda: self.clicked1()).pack()
        self.label = Label (self.root, text="")
        self.label.pack()

        self.quitbutton = Button(self.root, text="Quit", command=self.kill_windows)
        self.quitbutton.pack(side=LEFT)

        self.cp_button = Button(self.root, text='Copy', command=self.copy_to_clip).pack(side=LEFT)
        self.root.update()
        self.root.mainloop()

    def copy_to_clip(self):

        self.clip = Tk()
        self.clip.withdraw()
        self.clip.clipboard_clear()
        self.clip.clipboard_append(self.cpofpass)
        self.clip.update()
        self.clip.destroy()

    def clicked1(self):

        uinput = self.entrytext.get()
        anwser = PassChecker()

        try:
            num = int(uinput)
            if num >= 4:
                anwser.finalcheck(num)
                result = str(anwser.password)

            else:

                self.error_pop_up("Passwords must be at least 4 characters long. ")
                result = ''

        except ValueError:
            if uinput == "":
                self.error_pop_up("Input cannot be blank. ")
                result = ""
            elif uinput == "cat mainzer":
                self.error_pop_up("Good taste in art detected. ")
                result = "Have Fun Kiddos "
                webbrowser.open('http://mousebreath.com/did-you-know-mainzer-cats-were-not-drawn-by-mainzer/')
            else:
                self.error_pop_up("Please enter numbers only. ")
                result = ""

        self.cpofpass = str(result)
        # print('Result: ',result,'Copy: ',self.cpofpass)
        self.root.update()
        self.label.configure(text=result)

    def error_pop_up(self, errormessage):
        x = self.root.winfo_rootx()
        y = self.root.winfo_rooty()
        height = self.root.winfo_height()
        geom = "+%d+%d" % (x+30, y-1)

        self.popup = Tk()
        self.popup.attributes('-topmost', True)
        self.popup.geometry(geom)
        self.popup.wm_title("Error Message")
        errormessage = Label(self.popup, text=errormessage).pack()
        killbutton = Button(self.popup, text='OK', command=self.popup.destroy).pack(side=RIGHT)

    def kill_windows(self):

        try:
            self.popup.destroy()
        except (AttributeError, TclError):
            pass

        self.root.destroy()


App()

