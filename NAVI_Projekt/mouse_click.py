#!/usr/bin/python
from random import choice
import tkinter
root = tkinter.Tk()
root.title("root")
root.geometry("400x400+200+200")
# Code to add widgets will go here...

sceltavecchia = ""
colori = ['red','yellow','green','azure',"blue","coral","gold"]
def changecolor(event):
	global colori, sceltavecchia
	if sceltavecchia != "":
		colori.pop(colori.index(sceltavecchia))
		scelta = choice(colori)
		colori.append(sceltavecchia)
	else:
		scelta = choice(colori)
	root['bg'] = scelta
	sceltavecchia = scelta

label = tkinter.Label(root, text="Click where you want to change color")
label.pack(fill=tkinter.BOTH)


root.bind("<Button-1>", changecolor)
root.mainloop()