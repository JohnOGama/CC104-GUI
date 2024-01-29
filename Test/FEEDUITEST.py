import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

app = ctk.CTk()
app.geometry("500x500")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

items = [
]

def backToFeedHandler(root=None):
    global feed_frame
    if feed_frame:
        feed_frame.destroy()
    FeedUI()     

def add_item(title):
    new_item = {"Title": title}
    items.append(new_item)
    print("added item", title, items)
    messagebox.showinfo("added")
    itemsUI()

def itemsUI(root=None):
    for widget in feed_frame.winfo_children():
        widget.destroy()
    total_height = len(items) * 10 + (len(items) - 1) * 10
    center_y = (feed_frame.winfo_reqheight() - total_height) / 2

    for item in items:
        labelTest = ctk.CTkLabel(feed_frame, text=item["Title"])
        labelTest.pack(pady=12, padx=10, anchor=tk.W)
        labelTest.place(relx=0.5, rely=center_y / feed_frame.winfo_reqheight(), anchor=tk.CENTER)
        center_y += 13



    done_button = ctk.CTkButton(feed_frame, text="Back to feed", command=lambda: backToFeedHandler())
    done_button.pack()
    done_button.place(relx=0.1, rely=0.1, anchor=tk.CENTER)



def FeedUI(login_frame=None, username=None, itemsUI=None):

    # if login_frame:
    # login_frame.destroy()
    # if username:
    if itemsUI:
        itemsUI.destroy()
    global feed_frame
    feed_frame = ctk.CTkFrame(master=app)
    app.geometry("1000x600")
    feed_frame.pack(fill="both", expand=True)

    title = ctk.CTkLabel(master=feed_frame, text="Expense Tracker", font=("Roboto", 15), bg_color="white",
                         text_color="black", width=230)
    title.pack(pady=20, padx=10)
    title.place(relx=0.1, rely=0.1, anchor=tk.CENTER)

    label = ctk.CTkLabel(master=feed_frame, text=f"Hi , hope you doing well", font=("Roboto", 15))
    label.pack(pady=20, padx=10)
    label.place(relx=0.2, rely=0.2, anchor=tk.CENTER)

    screen_name = ctk.CTkLabel(master=feed_frame, text="Ogama", font=("Roboto", 15))
    screen_name.pack(pady=20, padx=10)
    screen_name.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

    logout_button = ctk.CTkButton(master=feed_frame, text="Logout", height=30, width=80, font=("Roboto", 15),
                                  fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
    logout_button.pack(pady=12, padx=10)
    logout_button.place(relx=0.88, rely=0.1, anchor=tk.CENTER)

    setting_button = ctk.CTkButton(master=feed_frame, text="⚙️", height=30, width=40, font=("Roboto", 15),
                                  fg_color="#BB85FF", text_color="black", hover_color="#dabfff")
    setting_button.pack(pady=12, padx=10)
    setting_button.place(relx=0.95, rely=0.1, anchor=tk.CENTER)

    # total_height = len(items) * 12 + (len(items) - 1) * 10
    # center_y = total_height / 2

    # for item in items:
    #     labelTest = ctk.CTkLabel(feed_frame, text=item["Title"])
    #     labelTest.pack(pady=12, padx=10, anchor=tk.W)
    #     labelTest.place(relx=0.5, rely=center_y / feed_frame.winfo_reqheight(), anchor=tk.CENTER)
    #     center_y += 13

    label_item = ctk.CTkLabel(feed_frame, text="Item:")
    label_item.pack()
    label_item.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    item_entry = ctk.CTkEntry(feed_frame)
    item_entry.pack()
    item_entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

    price_entry = ctk.CTkEntry(feed_frame)
    price_entry.pack()
    price_entry.place(relx=0.5, rely=0.47, anchor=tk.CENTER)
    quantity_entry = ctk.CTkEntry(feed_frame)
    quantity_entry.pack()
    quantity_entry.place(relx=0.5, rely=0.54, anchor=tk.CENTER)

    done_button = ctk.CTkButton(feed_frame, text="Done", command=lambda: add_item(item_entry.get()))
    done_button.pack()
    done_button.place(relx=0.5, rely=0.61, anchor=tk.CENTER)

FeedUI()
app.mainloop()
