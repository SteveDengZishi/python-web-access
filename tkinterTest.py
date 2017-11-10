#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:59:37 2017

@author: stevedeng
"""

import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk,Image

class ClickerApp():
    
    def __init__(self, root):
        #create two Buttons one at the top, one at the bottom
        self.button = tk.Radiobutton(root,text = "hihihi",value=0)
        self.button.pack(side = tk.LEFT)
        self.but = ttk.Button(root, text = "WhatUp", command = lambda: self.displayWhatUp(root))
        self.but.pack(side = tk.TOP)
        self.but2 = ttk.Button(root, text = "ShutUp", command = lambda: self.displayShutUp())
        self.but2.pack(side = tk.BOTTOM)
        
        self.butList=[]
        
        #dropdown combobox with selections
        self.options=tk.StringVar()
        self.menu = ttk.Combobox(root, state = "readonly", textvariable = self.options)
        self.menu.pack()
        self.menu.config(values=("a","b","c"))
        self.menu.current(0)
        
        #button = tk.Radiobutton(root,text = "hihihi",value=1).pack(side = tk.LEFT)
        #bar2 = tk.OptionMenu(root,variable = 3, value = [1,2,3] ).grid(row = 0, column = 2)
        #bar = tk.OptionMenu(root,variable = 3, value = [1,2,3] ).pack(side = tk.RIGHT)
        #bar3 = tk.OptionMenu(root,variable = 3, value = [1,2,3] ).place(x = 100, y = 300)
        
    def displayWhatUp(self,root):
        self.button = tk.Radiobutton(root,text = "hihihi",value=0)
        self.button.pack(side = tk.LEFT)
        self.butList.append(self.button)
        #self.label.configure(text = "Heeeeeyyyyy, WHATUPPPPP!")
    def displayShutUp(self):
        if(len(self.butList)!=0):
            self.button = self.butList[-1]
            self.butList=self.butList[:-1]
            self.button.pack_forget()
        #text.configure(text = "YOOOOO, SHUTUPPPPP!")
        #text.configure(background="#CCCCFF")
        return
         
def main():
    root = tk.Tk()
    root.geometry("500x750")
    root.title("Clickers")
    root.configure(background='#CCCCFF')
    app = ClickerApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()