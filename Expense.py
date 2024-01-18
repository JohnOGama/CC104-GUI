import tkinter as tk
from tkinter import messagebox

def add_expense():
    item = item_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()

    if not item or not price or not quantity:
        messagebox.showwarning("Incomplete Information", "Please enter all details.")
        return

    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for price and quantity.")
        return

    expense = {"Item": item, "Price": price, "Quantity": quantity}
    expenses_list.append(expense)

    # Clear the entry fields for the next entry
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def show_expenses():
    if not expenses_list:
        messagebox.showinfo("Expenses", "No expenses recorded yet.")
    else:
        expenses_text = "\n".join([f"{expense['Item']}: ${expense['Price']} x {expense['Quantity']}" for expense in expenses_list])
        messagebox.showinfo("Expenses", expenses_text)

def create_gui():
    global item_entry, price_entry, quantity_entry, expenses_list

    root = tk.Tk()
    root.title("Expense Tracker")

    # GUI components
    label_item = tk.Label(root, text="Item:")
    label_item.pack()

    item_entry = tk.Entry(root)
    item_entry.pack()

    label_price = tk.Label(root, text="Price:")
    label_price.pack()

    price_entry = tk.Entry(root)
    price_entry.pack()

    label_quantity = tk.Label(root, text="Quantity:")
    label_quantity.pack()

    quantity_entry = tk.Entry(root)
    quantity_entry.pack()

    done_button = tk.Button(root, text="Done", command=add_expense)
    done_button.pack()

    show_button = tk.Button(root, text="Show Expenses", command=show_expenses)
    show_button.pack()

    expenses_list = []

    root.mainloop()

# Call the function to create and run the GUI
create_gui()
