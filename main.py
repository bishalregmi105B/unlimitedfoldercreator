from cgitb import text
import os
import threading 
import tkinter

root = tkinter.Tk()
root.title("GUI Folder Creator")
root.geometry("720x420")

valu = tkinter.StringVar()

def createandout():
    for i in range(int(valu.get())):
        textbox.insert(tkinter.END, f"{i}st folder is created \n")
        os.mkdir(f"{i}st")

def startact():
    t1=threading.Thread(target=createandout())
    t1.start()

txtinp = tkinter.Entry(textvariable=valu)
txtinp.pack()

btn = tkinter.Button(text="Genrate FOlders ",command=startact,background="Gray",foreground="Pink")
btn.pack()

#############################Text Area
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side= tkinter.RIGHT, fill= tkinter.Y)
textbox =  tkinter.Text(root)
textbox.pack()
# attach textbox to scrollbar
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)
########################finsh

root.mainloop()