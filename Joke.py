from tkinter import *
from tkinter import messagebox
import random
#hi

def no():
    messagebox.showinfo('','Так и знал !')
    quit()

def motionMause(event):
    btnn.place(x = random.randint(0,500),y = random.randint(0,500))


win = Tk()
win.geometry("600x600")
win.title("Важный опрос")
win.resizable(width = False , height= False)
win.config(bg = '#7f81b3')

label = Label(win,text="Ты Лох ?",font="Arial 21 bold",bg = '#7f81b3').pack()
btnn = Button(win,text="Нет",font="Arial 21 bold",bg = '#7f81b3',padx=5,pady=5)
btnn.place(x=170,y=100)
btnn.bind("<Enter>",motionMause)
button_1 = Button(win,text="Да",font="Arial 21 bold",bg = '#7f81b3',command=no).place(x=350,y=100)



win.mainloop()