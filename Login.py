import customtkinter as ctk
# from components.Feed import FeedUI
from tkinter import messagebox

users = {}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

items = []

# To add items into array, used items.append({"Item": itemAdded, "Price": priceAdded, "Quantity":quantityAdded})


root = ctk.CTk()
root.geometry("600x500")
root.title("Login/Register")

def FeedUI(  login_frame=None, username=None):
    if login_frame:
        login_frame.destroy()



    if username:
        global feed_frame
        feed_frame = ctk.CTkFrame(master=root)
        feed_frame.pack(pady=20, padx=60, fill="both", expand=True)

        label = ctk.CTkLabel(master=feed_frame, text="FEED")
        label.pack(pady=20, padx=10)

        label = ctk.CTkLabel(master=feed_frame,text=f"Hi {username}, hope you doing well", font=("Roboto", 30))
        label.pack(pady=20, padx=10)

        back_button = ctk.CTkButton(master=feed_frame, text="Logout", command=lambda: LogInUI(root,  register_frame, feed_frame), height=40, width=200, font=("Roboto", 15))
        back_button.pack(pady=12, padx=10)


def LogInUI(root, register_frame,feed_frame ):
    if register_frame:
        register_frame.destroy()
    if feed_frame:
        feed_frame.destroy()

    global login_frame
    login_frame = ctk.CTkFrame(master=root)
    login_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=login_frame, text="Login", font=("Roboto", 20))
    label.pack(pady=20, padx=10)

    username_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Username", height=40, width=200, font=("Roboto", 15))
    username_entry.pack(pady=12, padx=10)

    password_entry = ctk.CTkEntry(master=login_frame, placeholder_text="Password", show="*", height=40, width=200, font=("Roboto", 15))
    password_entry.pack(pady=12, padx=10)

    login_button = ctk.CTkButton(master=login_frame, text="Login", command=lambda: login(root, username_entry, password_entry), height=40, width=200, font=("Roboto", 15))
    login_button.pack(pady=12, padx=10)

    register_button = ctk.CTkButton(master=login_frame, text="Register", command=lambda: RegisterUI(root, login_frame), height=40, width=200, font=("Roboto", 15))
    register_button.pack(pady=12, padx=10)

def RegisterUI(root, login_frame):
    login_frame.destroy()

    global register_frame
    register_frame = ctk.CTkFrame(master=root)
    register_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=register_frame, text="Register", font=("Roboto", 20))
    label.pack(pady=20, padx=10)

    new_username_entry = ctk.CTkEntry(master=register_frame, placeholder_text="New Username", height=40, width=200, font=("Roboto", 15))
    new_username_entry.pack(pady=12, padx=10)

    new_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="New Password", show="*", height=40, width=200, font=("Roboto", 15))
    new_password_entry.pack(pady=12, padx=10)

    register_button = ctk.CTkButton(master=register_frame, text="Register", command=lambda: registerHandler(root, new_username_entry, new_password_entry), height=40, width=200, font=("Roboto", 15))
    register_button.pack(pady=12, padx=10)

    back_button = ctk.CTkButton(master=register_frame, text="Back to Login", command=lambda: LogInUI(root, register_frame, None), height=40, width=200, font=("Roboto", 15))
    back_button.pack(pady=12, padx=10)

def login(root, username_entry, password_entry):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username in users.values() and entered_password in users.values():
        print("Authorized")
        FeedUI(  login_frame, username=entered_username)     
    else:
        print("Invalid username or password")

def registerHandler( root, new_username_entry, new_password_entry):
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username in users:
        print("Username already exists")

    if new_username and new_password:
        users.update({"Username":new_username, "Password":new_password})
        messagebox.showinfo("Successful", "Registration successful")
        LogInUI(root, register_frame, None)
        print("Registered ", users)
    else: 
        messagebox.showwarning("Warning", "Please enter a username and password")
        print()

LogInUI(root, None, None)
root.mainloop()

