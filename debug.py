# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 13:06:32 2018

"""

import glob

str_pattern = "C:/Users/306235/Documents/_Temp/**/*.svg"

list_temp = glob.glob(str_pattern, recursive=True)

for item in list_temp:

    print(item)

# import os

# os.startfile('c:/')

# import gsyIO

# gsyIO.open_folder('c:/')

# import glob

# str_pattern = "C:/Users//Documents/_Temp/**/*.svg"

# for item in glob.iglob(str_pattern, recursive=True):

#     print(item)

#from  tkinter import *
#import tkinter, tkconstants, tkFileDialog
#root = Tk()
#root.directory = tkFileDialog.askdirectory()
#print (root.directory)

# import gsyIO

# str_folder = gsyIO.get_dir()

# print('The selected folder is : ' + str_folder)