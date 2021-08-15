from tkinter import*

root=Tk()
root.title("Calculator")
e=Entry(root,width=40,borderwidth=5,justify=RIGHT )
e.grid(row=0,column=0,columnspan=6,padx=25,pady=0)

def button_click(number):
    e.insert(END,number)

def calculate():
    ans=eval(e.get())
    e.delete(0,END)
    e.insert(END,ans)


b1=Button(root,text="1",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(1),font=('arial', 10, 'bold'),)
b2=Button(root,text="2",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(2),font=('arial', 10, 'bold'),)
b3=Button(root,text="3",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(3),font=('arial', 10, 'bold'),)
b4=Button(root,text="4",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(4),font=('arial', 10, 'bold'),)
b5=Button(root,text="5",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(5),font=('arial', 10, 'bold'),)
b6=Button(root,text="6",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(6),font=('arial', 10, 'bold'),)
b7=Button(root,text="7",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(7),font=('arial', 10, 'bold'),)
b8=Button(root,text="8",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(8),font=('arial', 10, 'bold'),)
b9=Button(root,text="9",padx=35,pady=20,bg="grey",fg="yellow",command=lambda:button_click(9),font=('arial', 10, 'bold'),)
b0=Button(root,text="0",padx=34,pady=20,bg="grey",fg="yellow",command=lambda:button_click(0),font=('arial', 10, 'bold'),)

b_add=Button(root,text="+",padx=34,pady=19,bg="grey",fg="yellow",command=lambda:button_click("+"),font=('arial', 10, 'bold'),)
b_subtract=Button(root,text="-",padx=34,pady=20,bg="grey",fg="yellow",command=lambda:button_click("-"),font=('arial', 10, 'bold'),)
b_multiplu=Button(root,text="x",padx=34,pady=20,bg="grey",fg="yellow",command=lambda:button_click("*"),font=('arial', 10, 'bold'),)
b_division=Button(root,text="÷",padx=34,pady=20,bg="grey",fg="yellow",command=lambda:button_click("/"),font=('arial', 10, 'bold'),)
button_clear=Button(root,text="AC",padx=34,pady=20,bg="grey",fg="yellow",command=lambda:e.delete(0,END),font=('arial', 10, 'bold'),)
b_calculate=Button(root,text="=",padx=34,pady=20,bg="grey",fg="yellow",command=calculate,font=('arial', 10, 'bold'),)


b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

b_add.grid(row=1,column=4)
b_subtract.grid(row=2,column=4)
b_multiplu.grid(row=3,column=4)
b_division.grid(row=4,column=4)
button_clear.grid(row=4,column=1)
b_calculate.grid(row=4,column=2)

















root.mainloop()