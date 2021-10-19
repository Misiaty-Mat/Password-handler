from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# Func


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(4, 8))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    temp_pass = pass_letters + pass_numbers + pass_symbols
    shuffle(temp_pass)
    password = ''.join(temp_pass)
    password_input.delete(0, 'end')
    password_input.insert(END, password)
    pyperclip.copy(password)


def find_data():
    webside = webside_input.get()
    try:
        with open("data.json", 'r') as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Something went wrong.",
                            message="Data file not found.")
    else:
        if webside in json_data:
            email_login = json_data[webside]["e-mail/login"]
            password = json_data[webside]["password"]

            messagebox.showinfo(title="Your account data",
                                message=f"Here is your data for that account: \n E-mail/login: {email_login}\n Password: {password}")

            login_or_email_input.delete(0, 'end')
            password_input.delete(0, 'end')
            login_or_email_input.insert(END, email_login)
            password_input.insert(END, password)
        else:
            messagebox.showinfo(title="Something went wrong.",
                                message=f"Data for this {webside} does not exist.")


def save_data():
    webside = webside_input.get()
    email_login = login_or_email_input.get()
    password = password_input.get()
    new_data = {
        webside: {
            "e-mail/login": email_login,
            "password": password
        }
    }

    if len(webside) == 0 or len(password) == 0 or len(email_login) == 0:
        messagebox.showinfo(title="Something went wrong",
                            message="One of the fields is empty!")

    else:
        try:
            with open("data.json", 'r') as data_file:
                json_data = json.load(data_file)
                json_data.update(new_data)

        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            with open("data.json", 'w') as data_file:
                json.dump(json_data, data_file, indent=4)

        finally:
            webside_input.delete(0, 'end')
            password_input.delete(0, 'end')
            webside_input.focus()


FONT_DATA = ("Courier", 12)

window = Tk()
window.title("Passwords mamager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0, columnspan=2)

webside_banner = Label(text="Webside:")
webside_banner.grid(column=0, row=1)

login_or_email_banner = Label(text="Login/E-mail:")
login_or_email_banner.grid(column=0, row=2)

password_banner = Label(text="Password:")
password_banner.grid(column=0, row=3)

webside_input = Entry(width=18)
webside_input.grid(column=1, row=1, sticky=W, columnspan=2)
webside_input.focus()

login_or_email_input = Entry(width=35)
login_or_email_input.grid(column=1, row=2, sticky=W, columnspan=2)

password_input = Entry(width=17)
password_input.grid(column=1, row=3, sticky=E)

search_btn = Button(text="Search", width=13, command=find_data)
search_btn.grid(column=2, row=1)

gen_password_btn = Button(text="Generate password", command=generate_password)
gen_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
