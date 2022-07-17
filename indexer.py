import os
import tkinter as tk
import tkinter.filedialog as fdi
from tkinter import filedialog


def list_files():
    root = tk.Tk()
    startpath = filedialog.askdirectory()
    print(startpath)

    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        
        
        for f in files:
            file_object = open('indexOutput.txt', 'a')
            #file_object.write("Is it working?")
            file_object.write(('{}{}'.format(subindent, f)) + "\n")
            #print('{}{}'.format(subindent, f))
            file_object.close()

list_files()