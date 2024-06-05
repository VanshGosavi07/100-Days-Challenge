from tkinter import *

obj = Tk()
obj.title("Practice")
obj.minsize(width=400, height=400)
obj.config(padx=20,pady=20)
label = Label(text="Vansh", font=('Arial', 24, 'bold'))
label.grid(row=0, column=0)

new_button=Button(text="click me")
new_button.grid(row=0,column=2)

input = Entry()
input.grid(row=2, column=3)
input.insert(END, '@gmail.com')


def clicked_button():
    label.config(text=input.get())


button = Button(text='click me', command=clicked_button)
button.grid(row=1, column=1)
obj.mainloop()
