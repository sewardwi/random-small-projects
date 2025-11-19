import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def clear():
    entry.delete(0, tk.END)

def add_to_display(text):
    entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Complex Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for numbers and operators
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3),
    ('C', 5, 0), ('+', 5, 1)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                       command=lambda t=text: add_to_display(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Function to handle pressing the Enter key
def on_enter(event):
    calculate()

# Bind the Enter key to the calculate function
root.bind('<Return>', on_enter)

# Start the GUI
root.mainloop()
