import os
import tkinter as tk
from tkinter import ttk

def add_product():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if date and category and amount:
        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{amount}\n")
        status_label.config(text="Expense added successfully!", fg="green")
        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        Show()
    else:
        status_label.config(text="Please fill all the fields!", fg="red")

def remove_product():
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        date, category, amount = item_text
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        with open("expenses.txt", "w") as file:
            for line in lines:
                if line.strip() != f"{date},{category},{amount}":
                    file.write(line)
        status_label.config(text="Expense deleted successfully!", fg="green")
        Show()
    else:
        status_label.config(text="Please select an expense to delete!", fg="red")

def Show():
    global expenses_tree
    if os.path.exists("expenses.txt"):
        total_expense = 0
        expenses_tree.delete(*expenses_tree.get_children())
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                expenses_tree.insert("", tk.END, values=(date, category, amount))
                total_expense += float(amount)
        total_label.config(text=f"Total Amount: {total_expense:.2f}")
    else:
        total_label.config(text="No expenses recorded.")
        expenses_tree.delete(*expenses_tree.get_children())


root = tk.Tk()
root.title("Expense Tracker")


date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Category:")
category_label.grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Product", command=add_product)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)


columns = ("Date", "Category", "Amount")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Category", text="Category")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)


total_label = tk.Label(root, text="")
total_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)


view_button = tk.Button(root, text="View product", command=Show)
view_button.grid(row=7, column=0, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete product", command=remove_product)
delete_button.grid(row=7, column=1, padx=5, pady=10)


if not os.path.exists("expenses.txt"):
    with open("expenses.txt", "w"):
        pass

Show()

root.mainloop()
