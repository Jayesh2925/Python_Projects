from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry('600x600')
label = Label(root, text='which country you want to travel in ?').pack()
country = ['india', 'aus','USA', 'germany']
var = StringVar()
new_var = var.set('nonewhere')
def travel ():
    tmsg.showinfo('lets travel ', f' we are boooking your flight to {var.get()}\n wish you a very happy journey , thanks for booking with us')
    
for x in range (4):
    Radiobutton(root, text = country[x],variable = var, value = country[x]).pack()
    
Button(root , text = 'lets trvel', command = travel).pack()
root.mainloop()
