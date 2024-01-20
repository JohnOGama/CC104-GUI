import customtkinter as ctk
# from components.Feed import FeedUI
from tkinter import messagebox
import tkinter as tk

users = {"Username": "1", "Password": 1}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

items = []

todos = {}

# To add items into array, used items.append({"Item": itemAdded, "Price": priceAdded, "Quantity":quantityAdded})


root = ctk.CTk()
root.geometry("600x500")
root.title("Login/Register")

def FeedUI(  login_frame=None, username=None, itemsUI=None):
    if login_frame:
        login_frame.destroy()
    if username:
        
        global feed_frame
        feed_frame = ctk.CTkFrame(master=root)
        feed_frame.pack(fill="both", expand=True)

        screen_name = ctk.CTkLabel(master=feed_frame, text=f"{username}", font=("Roboto", 15))
        screen_name.pack(pady=20, padx=10)
        screen_name.place(relx=0.66, rely=0.1, anchor=tk.CENTER)

        logout_button = ctk.CTkButton(master=feed_frame, text="Logout", height=30, width=80,command=lambda: logoutHandler(root, register_frame, feed_frame), font=("Roboto", 15),
                                    fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
        logout_button.pack(pady=12, padx=10)
        logout_button.place(relx=0.78, rely=0.1, anchor=tk.CENTER)

        setting_button = ctk.CTkButton(master=feed_frame, text="⚙️", height=30, width=40, font=("Roboto", 15),
                                    fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
        setting_button.pack(pady=12, padx=10)
        setting_button.place(relx=0.90, rely=0.1, anchor=tk.CENTER)

        label = ctk.CTkLabel(master=feed_frame, text=f"Hi {username}, hope you doing well", font=("Roboto", 15))
        label.pack(pady=20, padx=10)
        label.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        title_label = ctk.CTkLabel(feed_frame, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(100, 20))

        scrollable_frame = ctk.CTkScrollableFrame(feed_frame, width=500, height=200)
        scrollable_frame.pack()

        entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
        entry.pack(fill="x")

        add_button = ctk.CTkButton(feed_frame, text="Add", width=500, command=lambda: add_todo(entry, scrollable_frame))
        add_button.pack(pady=20)

        delete_all_button = ctk.CTkButton(root, text="Delete All", width=500, command=lambda: delete_all(scrollable_frame))
        delete_all_button.pack(pady=10)

        


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

    global name_entry

    new_username_entry = ctk.CTkEntry(master=register_frame, placeholder_text="New Username", height=40, width=200, font=("Roboto", 15))
    new_username_entry.pack(pady=12, padx=10)

    new_password_entry = ctk.CTkEntry(master=register_frame, placeholder_text="New Password", show="*", height=40, width=200, font=("Roboto", 15))
    new_password_entry.pack(pady=12, padx=10)

    register_button = ctk.CTkButton(master=register_frame, text="Register", command=lambda: registerHandler(root, new_username_entry, new_password_entry), height=40, width=200, font=("Roboto", 15))
    register_button.pack(pady=12, padx=10)

    back_button = ctk.CTkButton(master=register_frame, text="Back to Login", command=lambda: LogInUI(root, register_frame, None), height=40, width=200, font=("Roboto", 15))
    back_button.pack(pady=12, padx=10)

def logoutHandler(root, register_frame, feed_frame):
    yes = messagebox.askyesno(message="Do you want to logout?")
    if yes: 
        LogInUI(root,  register_frame, feed_frame)

def login(root, username_entry, password_entry):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username in users.values() and entered_password in users.values():
        print("Authorized")
        messagebox.showinfo("Successful", "Log in success")
        FeedUI(  login_frame, username=entered_username)
    else:
        print("Invalid username or password")
        messagebox.showerror("Warning", "Wrong username or password")
        

def registerHandler(root, new_username_entry, new_password_entry):
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username and new_password:
        users.update({"Username":new_username, "Password":new_password})
        messagebox.showinfo("Successful", "Registration successful")
        LogInUI(root, register_frame, None)
        print("Registered", users)
    else:
        messagebox.showwarning("Warning", "Please enter a username and password")
        print("Invalid input")

def delete_all(scrollable_frame):
    for label in todos:
        label.destroy()  # Destroy each label
    todos.clear()

def add_todo(entry, scrollable_frame):
    todo = entry.get()
    if todo:
        label = ctk.CTkLabel(scrollable_frame, text=todo)
        label.pack()
        todos[label] = todo  # Store the label in the dictionary
        entry.delete(0, ctk.END)
LogInUI(root, None, None)

root.mainloop()

