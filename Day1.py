#import Library

from tkinter import*

#create window
root=Tk()
root.iconbitmap('Tkinter-\LOGO.ico')
root.title("Day 1 tkinter")

#full screen

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry('{}x{}+0+0'.format(width,height))

root.mainloop()