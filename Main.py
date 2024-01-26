import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk, messagebox



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

#Local Databases
users = [{"Username": "admin", "Password": "admin"},{"Username": "1", "Password": "1"}]
students = [
    ('John Doe', 'Engineering', 1, 'john@example.com', '123 Main St'),
    ('Alice Smith', 'Physics', 5, 'alice@example.com', '456 Oak St'),
    ('Bob Johnson', 'Computer Science', 2, 'bob@example.com', '789 Maple St'),
    ('Emma Brown', 'Mathematics', 1, 'emma@example.com', '101 Pine St'),
    ('Charlie Davis', 'Biology', 3, 'charlie@example.com', '202 Cedar St'),
    ('Eva White', 'Chemistry', 4, 'eva@example.com', '303 Birch St'),
    ('Frank Miller', 'History', 2, 'frank@example.com', '404 Elm St'),
    ('Grace Turner', 'Geology', 7, 'grace@example.com', '505 Spruce St'),
    ('Henry Wilson', 'Statistics', 5, 'henry@example.com', '606 Oakwood St'),
    ('Ivy Robinson', 'Environmental Science', 3, 'ivy@example.com', '707 Pine Lane'),
    ('Jack Evans', 'Political Science', 4, 'jack@example.com', '808 Maple Lane'),
    ('Katherine Hall', 'Sociology', 6, 'katherine@example.com', '909 Cedar Lane'),
    ('Liam Mitchell', 'Economics', 2, 'liam@example.com', '1010 Birch Lane'),
    ('Mia Turner', 'English', 4, 'mia@example.com', '1111 Elm Lane'),
    ('Noah Wright', 'Psychology', 1, 'noah@example.com', '1212 Spruce Lane'),
    ('Olivia Reed', 'Philosophy', 6, 'olivia@example.com', '1313 Oakwood Lane'),
    ('Peter Foster', 'Art History', 8, 'peter@example.com', '1414 Maplewood Lane'),
    ('Quinn Parker', 'Communication', 7, 'quinn@example.com', '1515 Cedarwood Lane'),
    ('Rachel Hayes', 'Music', 11, 'rachel@example.com', '1616 Birchwood Lane'),
    ('Samuel White', 'Math Education', 14, 'samuel@example.com', '1717 Elmwood Lane')
]

# Print the generated students
for student in students:
    print(student)

items = []
todos = {}

root = ctk.CTk()
root.geometry("600x500")
root.title("Login/Register")

new_fname = "default"

style = ttk.Style(root)
style.configure("Treeview", background="#414a4c", 
                fieldbackground="black", foreground="white")

style.configure("Treeview.Heading", background="lightgreen", 
                foreground="black", relief="flat")


if not new_fname:
    new_fname = "John"

def FeedUI(login_frame=None, username=None, settings_frame=None):
    if login_frame:
        login_frame.destroy()

    if username:
        root.geometry("1000x500")
        feed_frame = ctk.CTkFrame(root)
        feed_frame.pack(fill="both", expand=True)

        screen_name = tk.Label(feed_frame, text=f"{new_fname}", font=("Roboto", 15))
        screen_name.pack(pady=20, padx=10)
        screen_name.place(relx=0.66, rely=0.1, anchor=tk.CENTER)

        # logout_button = tk.Button(feed_frame, text="Logout", height=30, width=80,
                                  
        #                           font=("Roboto", 15), fg="#BB85FF", bg="white", activebackground="#dabfff")
        # logout_button.pack(pady=12, padx=10)
        # logout_button.place(relx=0.78, rely=0.1, anchor=tk.CENTER)

        label = tk.Label(feed_frame, text=f"Hi {new_fname}, hope you're doing well", font=("Roboto", 15))
        label.pack(pady=20, padx=10)
        label.place(relx=0.2, rely=0.1, anchor=tk.CENTER)

        global student_tree, search_entry

        show_button = ctk.CTkButton(feed_frame, text="Show Students", command=show_students_in_treeview)
        show_button.place(relx=0.3, rely=0.2, anchor=tk.CENTER)

        search_entry = ctk.CTkEntry(feed_frame)
        search_entry.pack()
        search_entry.place(relx=0.1, rely=0.2, anchor=tk.CENTER)
        search_button = ctk.CTkButton(feed_frame, text="Search Students", command=search_students)
        search_button.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

        sort_course_button = ctk.CTkButton(feed_frame, text="Sort by Course", command=sort_students_by_course)
        sort_course_button.pack()
        sort_course_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        sort_year_button = ctk.CTkButton(feed_frame, text="Sort by Year", command=sort_students_by_year)
        sort_year_button.pack()
        sort_year_button.place(relx=0.6, rely=0.2, anchor=tk.CENTER)


        student_tree = ttk.Treeview(feed_frame, columns=('Name', 'Course', 'Year', 'Email', 'Address'), 
        show='headings')
        student_tree.heading('Name', text='Name')
        student_tree.heading('Course', text='Course')
        student_tree.heading('Year', text='Year')
        student_tree.heading('Email', text='Email')
        student_tree.heading('Address', text='Address')
        student_tree.pack(pady=10, padx=10)
        student_tree.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        student_tree.tag_configure('Name', background='#add8e6')

        student_tree.column('Name', width=150)
        student_tree.column('Course', width=150)
        student_tree.column('Year', width=50)  # Adjust the width as needed
        student_tree.column('Email', width=200)
        student_tree.column('Address', width=250)

        show_students_in_treeview()

def SettingsUI(root=root, feed_frame=None, username=None, uPass=None, uE=None, uLn=None, uFn=None, uName=None):
    if feed_frame:
        print("Truee")
        feed_frame.destroy()

    if uPass and uE and uLn and uFn and uName:
        settings_frame = ctk.CTkFrame(master=root)
        settings_frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(master=settings_frame, text="Settings", font=("Roboto", 15))
        label.pack()
        label.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        title = ctk.CTkLabel(master=settings_frame, text="Edit UserProfile", font=("Roboto", 15))
        title.pack()
        title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        userFirstName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Firstname: {uFn}", font=("Roboto", 15), height=40, width=250)
        userFirstName.pack()
        userFirstName.place(relx=0.1, rely=0.3)

        userLastName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Lastname: {uLn}", font=("Roboto", 15), height=40, width=250)
        userLastName.pack()
        userLastName.place(relx=0.55, rely=0.3)

        userEmail = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Email: {uE}", font=("Roboto", 15), height=40, width=520)
        userEmail.pack()
        userEmail.place(relx=0.1, rely=0.4)

        userName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Username: {uName}", font=("Roboto", 15), height=40, width=520)
        userName.pack()
        userName.place(relx=0.1, rely=0.5)

        userPass = ctk.CTkEntry(master=settings_frame, show="*", font=("Roboto", 15), height=40, width=520)
        userPass.pack()
        userPass.place(relx=0.1, rely=0.6)

        save_button = ctk.CTkButton(settings_frame, text="Save", height=40, width=520, command=lambda: updateCredentials(username_to_update=username1, 
                                                                                                userName=userName, 
                                                                                                userPass=userPass, 
                                                                                                userFirstName=userFirstName,
                                                                                                userLastName=userLastName,
                                                                                                userEmail=userEmail,
                                                                                                settings_frame=settings_frame))
        save_button.pack()
        save_button.place(relx=0.1, rely=0.7)
    else:

        settings_frame = ctk.CTkFrame(master=root)
        settings_frame.pack(fill="both", expand=True)

        label = ctk.CTkLabel(master=settings_frame, text="Settings", font=("Roboto", 15))
        label.pack()
        label.place(relx=0.9, rely=0.1, anchor=tk.CENTER)

        title = ctk.CTkLabel(master=settings_frame, text="Edit UserProfile", font=("Roboto", 15))
        title.pack()
        title.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        userFirstName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Firstname: {new_fname}", font=("Roboto", 15), height=40, width=250)
        userFirstName.pack()
        userFirstName.place(relx=0.1, rely=0.3)

        userLastName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Lastname: {lname}", font=("Roboto", 15), height=40, width=250)
        userLastName.pack()
        userLastName.place(relx=0.55, rely=0.3)

        userEmail = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Email: {email}", font=("Roboto", 15), height=40, width=520)
        userEmail.pack()
        userEmail.place(relx=0.1, rely=0.4)

        userName = ctk.CTkEntry(master=settings_frame, placeholder_text=f"Username: {username1}", font=("Roboto", 15), height=40, width=520)
        userName.pack()
        userName.place(relx=0.1, rely=0.5)

        userPass = ctk.CTkEntry(master=settings_frame, show="*", font=("Roboto", 15), height=40, width=520)
        userPass.pack()
        userPass.place(relx=0.1, rely=0.6)

        save_button = ctk.CTkButton(settings_frame, text="Save", height=40, width=520, command=lambda: updateCredentials(username_to_update=username1, 
                                                                                                userName=userName, 
                                                                                                userPass=userPass, 
                                                                                                userFirstName=userFirstName,
                                                                                                userLastName=userLastName,
                                                                                                userEmail=userEmail,
                                                                                                settings_frame=settings_frame))
        save_button.pack()
        save_button.place(relx=0.1, rely=0.7)

        back_button = ctk.CTkButton(settings_frame, text="Back to feed", command=lambda: FeedUI(login_frame=None, username=None, settings_frame=settings_frame))
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
    login_frame.pack(fill="both", expand=True)

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
    register_frame.pack( fill="both", expand=True)

    label = ctk.CTkLabel(master=register_frame, text="Student Register", font=("Roboto", 20))
    label.pack(pady=20, padx=10)

    global name_entry, course_entry, year_entry, email_entry, address_entry
    name_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Name", height=40, width=250, font=("Roboto", 15))
    name_entry.pack(pady=12, padx=10)
    name_entry.place(relx=0.1, rely=0.2)

    year_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Year", height=40, width=250, font=("Roboto", 15))
    year_entry.pack(pady=12, padx=10)
    year_entry.place(relx=0.55, rely=0.2)

    course_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Course", height=40, width=520, font=("Roboto", 15))
    course_entry.pack(pady=12, padx=10)
    course_entry.place(relx=0.1, rely=0.3)

    email_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Email", height=40, width=520, font=("Roboto", 15))
    email_entry.pack(pady=12, padx=10)
    email_entry.place(relx=0.1, rely=0.4)

    address_entry = ctk.CTkEntry(master=register_frame, placeholder_text="Address", show="*", height=40, width=520, font=("Roboto", 15))
    address_entry.pack(pady=12, padx=10)
    address_entry.place(relx=0.1, rely=0.5)

    register_button = ctk.CTkButton(master=register_frame, text="Submit", command=submit)
    register_button.pack(pady=12, padx=10)
    register_button.place(relx=0.1, rely=0.6)

    back_button = ctk.CTkButton(master=register_frame, text="Back to Login", command=lambda: LogInUI(root, register_frame, None, None), height=40, width=520, font=("Roboto", 15))
    back_button.pack(pady=12, padx=10)
    back_button.place(relx=0.1, rely=0.7)

def submit():
    name = name_entry.get()
    course = course_entry.get()
    year = year_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and course and year and email and address:
        student_info = (name, course, year, email, address)
        students.append(student_info)
        clear_entries()
        messagebox.showinfo("Success", "Student registered successfully!")
        show_students_in_treeview()
    else:
        messagebox.showwarning("Incomplete Information", "Please fill in all fields.")

def clear_entries():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def show_students_in_treeview():
    student_tree.delete(*student_tree.get_children())
    for student in students:
        student_tree.insert('', 'end', values=student)

def search_students():
    search_term = search_entry.get().lower()
    results = [student for student in students if search_term in str(student).lower()]
    student_tree.delete(*student_tree.get_children())
    for result in results:
        student_tree.insert('', 'end', values=result)

def sort_students_by_course():
    students.sort(key=lambda x: x[1])
    show_students_in_treeview()

def sort_students_by_year():
    students.sort(key=lambda x: x[2])  
    show_students_in_treeview()

    
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
        

def registerHandler(root, new_username, new_password, new_firstName, new_lastName, new_email):
    global new_fname, lname, email, username1
    new_fname = new_firstName.get()
    lname = new_lastName.get()
    email = new_email.get()
    username1 = new_username.get()

    if new_username.get() and new_password.get() and new_email.get():
        isUserTaken = False
        for user in users:
            if user["Username"] == new_username.get():
                isUserTaken = True
                break
        if not isUserTaken:
            if "@gmail" in new_email.get():
                if new_fname.isalpha() and new_lastName.get().isalpha():
                    users.append({"Username": new_username.get(), "Password": new_password.get(), "FirstName": new_firstName.get(), "LastName": new_lastName.get(), "Email": new_email.get()})
                    messagebox.showinfo("Successful", "Registration successful")
                    LogInUI(root, register_frame, None, None)
                    print("Registered", users)
                else:
                    messagebox.showwarning("Warning", "Invalid first name or last name. Please avoid using numbers.")
            else:
                messagebox.showwarning("Warning", "Invalid email address. Please enter a valid email.")
        else:
            messagebox.showwarning("Warning", "Username already taken. Please choose a different one.")
    else:
        messagebox.showwarning("Warning", "Please enter a username, password, and a valid email address.")


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

def updateCredentials(username_to_update, userName, userPass, settings_frame, userFirstName, userLastName, userEmail):
    global new_fname, lname, email, username1
    new_fname = userFirstName.get()
    lname = userLastName.get()
    email = userEmail.get()
    username1 = userName.get()
    index = findUserIndex(username_to_update)
    if index:
        if userName and userPass and userEmail:
            # Check if the new username is already taken
            isUserTaken = isUsernameTaken(userName.get()) and userName.get() != username_to_update
            if not isUserTaken:
                if "@gmail" in email:
                    if userFirstName.get().isalpha() and userLastName.get().isalpha():
                        global uName, uPass, uFn, uLn, uE
                        uName = users[index]["Username"] = userName.get()
                        uPass = users[index]["Password"] = userPass.get()
                        uFn = users[index]["FirstName"] = userFirstName.get()
                        uLn = users[index]["LastName"] = userLastName.get()
                        uE = users[index]["Email"] = userEmail.get()
                        print("uName", uName)
                        messagebox.showinfo("Success", "Credentials updated successfully")
                        messagebox.showinfo("Redirecting", "You will be redirected to Login")
                        LogInUI(root, None, None, settings_frame=settings_frame)
                        print("New users", users)
                    else:
                        messagebox.showwarning("Warning", "Invalid first name or last name. Please avoid using numbers or special characters.")
                else:
                    messagebox.showwarning("Warning", "Invalid email address. Please enter a valid email.")
            else:
                messagebox.showwarning("Username taken", "The new username is already taken. Please choose a different one.")
        else:
            messagebox.showwarning("Warning", "Please enter a username, password, and email")
            print("Invalid input")
    else:
        messagebox.showinfo("No changes", "No changes were made")


def toggle_dark_mode(switch):
    if switch.get():
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")   



LogInUI(root, None, None)
root.mainloop()

