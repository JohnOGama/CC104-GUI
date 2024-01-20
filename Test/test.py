import customtkinter as ctk

def add_todo():
    todo = entry.get()
    if todo:
        label = ctk.CTkLabel(scrollable_frame, text=todo)
        label.pack()
        entry.delete(0, ctk.END)

# Main application window
root = ctk.CTk()
root.geometry("750x450")
root.title("Todo App")

# Title label
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

# Scrollable frame for todo list
scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
scrollable_frame.pack()

# Entry for adding todos
entry = ctk.CTkEntry(scrollable_frame, placeholder_text="Add todo")
entry.pack(fill="x")

# Button to add todo
add_button = ctk.CTkButton(root, text="Add", width=500, command=add_todo)
add_button.pack(pady=20)

# Start the application main loop
root.mainloop()
