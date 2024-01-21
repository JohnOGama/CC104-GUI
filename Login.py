import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Local Databases
users = []
items = []
todos = {}

root = ctk.CTk()
root.geometry("600x500")
root.title("Login/Register")

def FeedUI( login_frame=None, username=None, settings_frame=None):
    if login_frame:
        print("True")
        login_frame.destroy()
    if settings_frame:
        print("True")
        settings_frame.destroy()
        feed_frame = ctk.CTkFrame(master=root)
        feed_frame.pack(fill="both", expand=True)

        screen_name = ctk.CTkLabel(master=feed_frame, text=f"{uName}", font=("Roboto", 15))
        screen_name.pack(pady=20, padx=10)
        screen_name.place(relx=0.66, rely=0.1, anchor=tk.CENTER)

        logout_button = ctk.CTkButton(master=feed_frame, text="Logout", height=30, width=80,command=lambda: logoutHandler(root, register_frame, feed_frame), font=("Roboto", 15),
                                    fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
        logout_button.pack(pady=12, padx=10)
        logout_button.place(relx=0.78, rely=0.1, anchor=tk.CENTER)

        setting_button = ctk.CTkButton(master=feed_frame, text="⚙️", height=30, width=40, font=("Roboto", 15), fg_color="#BB85FF", text_color="black", hover_color="#dabfff", command=lambda: SettingsUI(root=root, feed_frame=feed_frame, username=username))
        setting_button.pack(pady=12, padx=10)
        setting_button.place(relx=0.90, rely=0.1, anchor=tk.CENTER)

        label = ctk.CTkLabel(master=feed_frame, text=f"Hi {uName}, hope you doing well", font=("Roboto", 15))
        label.pack(pady=20, padx=10)
        label.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        darkmode = ctk.CTkSwitch(feed_frame, width=80, text="LightMode", command=lambda: toggle_dark_mode(darkmode))
        darkmode.pack()
        darkmode.place(relx=0.15, rely=0.27, anchor=tk.CENTER)

        title_label = ctk.CTkLabel(feed_frame, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(100, 20))

        scrollable_frame = ctk.CTkScrollableFrame(feed_frame, width=500, height=200)
        scrollable_frame.pack()

        entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
        entry.pack(fill="x")

        add_button = ctk.CTkButton(feed_frame, text="Add", width=500, command=lambda: add_todo(entry, scrollable_frame))
        add_button.pack(pady=10)

        delete_all_button = ctk.CTkButton(feed_frame, text="Delete All", width=500, command=lambda: delete_all(scrollable_frame))
        delete_all_button.pack()
        
    if username:  
        feed_frame = ctk.CTkFrame(master=root)
        feed_frame.pack(fill="both", expand=True)

        screen_name = ctk.CTkLabel(master=feed_frame, text=f"{uName}", font=("Roboto", 15))
        screen_name.pack(pady=20, padx=10)
        screen_name.place(relx=0.66, rely=0.1, anchor=tk.CENTER)

        logout_button = ctk.CTkButton(master=feed_frame, text="Logout", height=30, width=80,command=lambda: logoutHandler(root, register_frame, feed_frame), font=("Roboto", 15),
                                    fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
        logout_button.pack(pady=12, padx=10)
        logout_button.place(relx=0.78, rely=0.1, anchor=tk.CENTER)

        setting_button = ctk.CTkButton(master=feed_frame, text="⚙️", height=30, width=40, font=("Roboto", 15), fg_color="#BB85FF", text_color="black", hover_color="#dabfff", command=lambda: SettingsUI(root=root, feed_frame=feed_frame, username=username))
        setting_button.pack(pady=12, padx=10)
        setting_button.place(relx=0.90, rely=0.1, anchor=tk.CENTER)

        label = ctk.CTkLabel(master=feed_frame, text=f"Hi {uName}, hope you doing well", font=("Roboto", 15))
        label.pack(pady=20, padx=10)
        label.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        
        # delete_todo = ctk.CTkEntry(feed_frame, width=70)
        # delete_todo.pack()
        # delete_todo.place(relx=0.13, rely=0.27, anchor=tk.CENTER)

        darkmode = ctk.CTkSwitch(feed_frame, width=80, text="LightMode", command=lambda: toggle_dark_mode(darkmode))
        darkmode.pack()
        darkmode.place(relx=0.15, rely=0.27, anchor=tk.CENTER)

        title_label = ctk.CTkLabel(feed_frame, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(100, 20))


        scrollable_frame = ctk.CTkScrollableFrame(feed_frame, width=500, height=200)
        scrollable_frame.pack()

        entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
        entry.pack(fill="x")

        add_button = ctk.CTkButton(feed_frame, text="Add", width=500, command=lambda: add_todo(entry, scrollable_frame))
        add_button.pack(pady=10)

        delete_all_button = ctk.CTkButton(feed_frame, text="Delete All", width=500, command=lambda: delete_all(scrollable_frame))
        delete_all_button.pack()

def SettingsUI(root=root, feed_frame=None, username=None):
    if feed_frame:
        print("Truee")
        feed_frame.destroy()
    settings_frame = ctk.CTkFrame(master=root)
    settings_frame.pack(fill="both", expand=True)
    label = ctk.CTkLabel(master=settings_frame, text=f"Settings", font=("Roboto", 15))
    label.pack()
    label.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

    title = ctk.CTkLabel(master=settings_frame, text="Edit UserProfile", font=("Roboto", 15))
    title.pack()
    title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    userLabel = ctk.CTkLabel(master=settings_frame, text=f"Username: {uName}", font=("Roboto", 15))
    userLabel.pack()
    userLabel.place(relx=0.46, rely=0.3, anchor=tk.CENTER)

    userName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"{uName}", font=("Roboto", 15))
    userName.pack()
    userName.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

    passLabel = ctk.CTkLabel(master=settings_frame, text=f"Password: ", font=("Roboto", 15))
    passLabel.pack()
    passLabel.place(relx=0.46, rely=0.42, anchor=tk.CENTER)

    userPass = ctk.CTkEntry(master=settings_frame,  show="*", font=("Roboto", 15))
    userPass.pack()
    userPass.place(relx=0.5, rely=0.47, anchor=tk.CENTER)

    save_button = ctk.CTkButton(settings_frame, text="Save", command=lambda: updateCredentials(username_to_update=uName, userName=userName, userPass=userPass, settings_frame=settings_frame))
    save_button.pack()
    save_button.place(relx=0.5, rely=0.56, anchor=tk.CENTER)



    back_button = ctk.CTkButton(settings_frame, text="Back to feed",command=lambda: FeedUI( login_frame=None, username=None, settings_frame=settings_frame) )
    back_button.pack()
    back_button.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

def LogInUI(root, register_frame,feed_frame, settings_frame=None ):
    if register_frame:
        register_frame.destroy()
    if feed_frame:
        feed_frame.destroy()
    if settings_frame:
        settings_frame.destroy()

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

    back_button = ctk.CTkButton(master=register_frame, text="Back to Login", command=lambda: LogInUI(root, register_frame, None, None), height=40, width=200, font=("Roboto", 15))
    back_button.pack(pady=12, padx=10)

def logoutHandler(root, register_frame, feed_frame):
    yes = messagebox.askyesno(message="Do you want to logout?")
    if yes: 
        LogInUI(root,  register_frame, feed_frame)

def login(root, username_entry, password_entry):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    authorized = False
    for user in users:
        if user["Username"] == entered_username and user["Password"] == entered_password:
            authorized = True
            break

    if authorized:
        print("Authorized")
        messagebox.showinfo("Successful", "Log in success")
        global uName, uPass
        uName = entered_username
        uPass = entered_password
        FeedUI(login_frame, username=entered_username)
    else:
        print("Invalid username or password")
        messagebox.showerror("Warning", "Wrong username or password")
        

def registerHandler(root, new_username_entry, new_password_entry):
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()

    if new_username and new_password:
        username_taken = False
        for user in users:
            if user["Username"] == new_username:
                username_taken = True
                break
        if not username_taken:
            users.append({"Username": new_username, "Password": new_password})
            messagebox.showinfo("Successful", "Registration successful")
            LogInUI(root, register_frame, None, None)
            print("Registered", users)
        else:
            messagebox.showwarning("Warning", "Username already taken. Please choose a different one.")
    else:
        messagebox.showwarning("Warning", "Please enter a username and password")
        print("Invalid input")

def findUserIndex(username_to_find):
    for i, user_info in enumerate(users):
        if user_info["Username"] == username_to_find:
            return i
    return -1

def isUsernameTaken(username):
    for user in users:
        if user["Username"] == username:
            return True
    return False

def updateCredentials(username_to_update, userName, userPass, settings_frame):
    index = findUserIndex(username_to_update)

    if index != -1:
        if userName and userPass:
            # Check if the new username is already taken
            username_taken = isUsernameTaken(userName.get()) and userName.get() != username_to_update

            if not username_taken:
                new_username = userName.get()
                new_password = userPass.get()

                users[index]["Username"] = new_username
                users[index]["Password"] = new_password

                messagebox.showinfo("Success", "Credentials updated successfully")
                messagebox.showinfo("Redirecting", "You will be redirected to Login")
                LogInUI(root, None, None, settings_frame=settings_frame)
            else:
                messagebox.showwarning("Username taken", "The new username is already taken. Please choose a different one.")
        else:
            messagebox.showwarning("Warning", "Please enter a username and password")
            print("Invalid input")
    else:
        messagebox.showwarning("User not found", f"User with Username '{username_to_update}' not found.")
        
# def deleteTodoByIndex(index):
#     if index in todos:
#         label_to_delete = todos[1]
#         print("label_to_delete", label_to_delete)
#         label_to_delete.destroy()
#         del todos[index]
#         messagebox.showinfo("Success", "Successful delete")
#     else:
#         label_to_delete = todos[index]
#         print("label_to_delete", label_to_delete)
#         label_to_delete.destroy()
#         del todos[index]
#         messagebox.showerror("Not found", "Not Found")
#         print("label_to_delete", label_to_delete)

def toggle_dark_mode(switch):
    if switch.get():
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")
        

def delete_all(scrollable_frame):
    for label in todos:
        label.destroy() 
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

