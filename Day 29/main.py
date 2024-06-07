from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    password = "".join(password_list)
    password_text.delete(0, END)
    password_text.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    website = website_text.get()
    email = email_text.get()
    password = password_text.get()

    if len(website) <= 0 or len(password) <= 0:
        messagebox.showinfo(title="Empty Information", message='Some of the field are empty')
    else:
        is_ok = messagebox.askyesno(title="Confirm Save",
                                    message=f"These are the details entered: \nWebsite: {website}\nEmail: {email}\nPassword: {password}\nIs it okay to save?")
        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_text.delete(0, END)
                password_text.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Generator")
screen.config(pady=50, padx=50)

# Logo image
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Labels and input fields
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_text = Entry(width=35)
website_text.focus()
website_text.grid(row=1, column=1, columnspan=2)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0, sticky="e")
email_text = Entry(width=35)
email_text.insert(END, '@gmail.com')
email_text.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_text = Entry(width=21)
password_text.grid(row=3, column=1)

# Buttons
generate_button = Button(text='Generate Password', command=password_generator)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=36, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

screen.mainloop()
