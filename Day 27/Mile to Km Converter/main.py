from tkinter import *

screen = Tk()
screen.maxsize(height=150, width=250)
screen.title('Miles To Km Converter')
screen.config(padx=30,pady=30)
user = Entry(width=10)
user.pack()
miles=km=0
label = Label(text=f'{miles} Miles is equal to {km} Km')
label.config(pady=10,padx=10)
label.pack()


def convertor():
    miles = int(user.get())
    km = miles * 1.609344
    label.config(text=f'{miles} Miles is equal to {round(km, 2)} Km')


button = Button(text='Calculate', font=('Times New Roman', 10, 'bold'), command=convertor)
button.pack()
screen.mainloop()
