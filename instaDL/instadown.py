import os
import instaloader
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sys

#win_crack = Tk()
#win_crack.geometry("250x250")
#win_crack.resizable = False
#win_crack.title = ("Insta Crack")

__author__="sn.lionel90"
print(__author__)

def picture_download(username):
    parser = instaloader.Instaloader()
    """Change the directory folder"""

    os.chdir(os.path.join(os.path.expanduser('~'), 'Downloads'))

    """Creates a new folder for insta downloads"""
    if os.path.isdir("Insta Donloads"):
        os.chdir("Insta Donloads")
        return parser.download_profile(username,profile_pic= True)

    else:
        """MAke dir if not exists"""
        os.mkdir("Insta Donloads")
        os.chdir("Insta Donloads")
        """Download the date"""

        return parser.download_profile(username, profile_pic= True)

if __name__ =="__main__":
    #win_crack.mainloop()
    user = input ("Enter Instagram Account: ")
    picture_download(user)
        