from tkinter import *

window=Tk() #Create an empty window
#Everything goes

def km_to_miles():
   print(e1_value.get()) #Because it is not an actual string, the get method converts it to a string
   miles=float(e1_value.get())*1.6 #Covert inputed value to miles
   t1.insert(END, miles)#textobject, insert at the end arg, put the value entered

b1=Button(window,text="Execute",command=km_to_miles) #Button class, takes lots of parameters (you can look them up using ipython, then from tkinter import*, then Button?
#b1.pack() #widget method to show the text button
b1.grid(row=0,column=0, rowspan=2) #Divides in grids the window, then you decide where to put the button

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value) #Entry text
e1.grid(row=0,column=1)

t1=Text(window, height=1,width=20)
t1.grid(row=0,column=2)


#Between theese two lines
window.mainloop()
