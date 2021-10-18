from tkinter import *
from tkinter import messagebox
from password_generator import gen_password
import pyperclip


def generate_password():
    password = gen_password()
    password_input.delete(0, 'end')
    password_input.insert(END, password)
    pyperclip.copy(password)


def save_data():
    webside = webside_input.get()
    email_login = login_or_email_input.get()
    password = password_input.get()

    if len(webside) == 0 or len(password) == 0:
        messagebox.showinfo(title="Something went wrong",
                            message="One of the fields is empty!")
    else:
        user_accept = messagebox.askokcancel(
            title=webside, message=f"Detail entered:\nWebside: {webside}\nE-mail/login: {email_login}\nPassword: {password}\nIs all correct?")

        if user_accept:
            webside_input.delete(0, 'end')
            password_input.delete(0, 'end')
            webside_input.focus()
            with open("data.txt", 'a') as file:
                file.write(f"{webside} / {email_login} / {password}\n")


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

webside_input = Entry(width=35)
webside_input.grid(column=1, row=1, columnspan=2)
webside_input.focus()

login_or_email_input = Entry(width=35)
login_or_email_input.grid(column=1, row=2, columnspan=2)
login_or_email_input.insert(END, "mat@wp.pl")

password_input = Entry(width=17)
password_input.grid(column=1, row=3, sticky=E)

gen_password_btn = Button(text="Generate password", command=generate_password)
gen_password_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=30, command=save_data)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
