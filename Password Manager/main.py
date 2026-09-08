import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import OK
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = []

    password_list += [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_list += [random.choice(NUMBERS) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Generated password: {password}")
    password_entry.insert(0, password)
    #window.clipboard_append(password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields.")
    else:
        resp = messagebox.askokcancel(website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password} \nIs it ok to save?", default=OK)
        if resp:
            with open("data.txt", "a") as file:
                data_str = website + " | " + email + " | " + password + "\n"
                file.write(data_str)
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("My Pass - Password Manager")
window.configure(background="white", padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:", fg="black", bg="white")
website_label.grid(row=1, column=0)

website_entry = tk.Entry(width=35, bg="white", fg="black")
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = tk.Label(text="Email/Username:", fg="black", bg="white")
email_label.grid(row=2, column=0)

email_entry = tk.Entry(width=35, bg="white", fg="black")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "piyushgoel17@gmail.com")

password_label = tk.Label(text="Password:", fg="black", bg="white")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(bg="white", width=21, fg="black")
password_entry.grid(row=3, column=1)

generate_password_button = tk.Button(text="Generate Password", bg="white", fg="black", highlightthickness=0,
                                     borderwidth=0, width=10, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(text="Add", bg="white", fg="black", highlightthickness=0, borderwidth=0,
                       width=32, command=save_to_file)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
