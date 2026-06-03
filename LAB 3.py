import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os

FILE_NAME = "expenses.csv"

# ---------------- FUNCTIONS ---------------- #

def add_expense():
    name = entry_name.get()
    category = combo_category.get()
    amount = entry_amount.get()
    date = entry_date.get()

    if name == "" or category == "" or amount == "" or date == "":
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        amount = float(amount)
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return
    except:
        messagebox.showerror("Error", "Invalid amount")
        return

    tree.insert("", "end", values=(name, category, amount, date))
    clear_fields()
    update_total()

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    combo_category.set("")

def delete_expense():
    selected = tree.selection()
    if not selected:
        messagebox.showerror("Error", "No item selected")
        return
    for item in selected:
        tree.delete(item)
    update_total()

def save_data():
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        for row in tree.get_children():
            writer.writerow(tree.item(row)["values"])
    messagebox.showinfo("Saved", "Data saved successfully!")

def load_data():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            tree.insert("", "end", values=row)
    update_total()

def update_total():
    total = 0
    for row in tree.get_children():
        total += float(tree.item(row)["values"][2])
    label_total.config(text=f"Total Expense: RM {total:.2f}")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("700x500")

tk.Label(root, text="Expense Name").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Category").grid(row=1, column=0)
combo_category = ttk.Combobox(root, values=["Food", "Transport", "Study", "Shopping", "Other"])
combo_category.grid(row=1, column=1)

tk.Label(root, text="Amount").grid(row=2, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=2, column=1)

tk.Label(root, text="Date").grid(row=3, column=0)
entry_date = tk.Entry(root)
entry_date.grid(row=3, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=4, column=0)
tk.Button(root, text="Delete", command=delete_expense).grid(row=4, column=1)
tk.Button(root, text="Save", command=save_data).grid(row=4, column=2)
tk.Button(root, text="Load", command=load_data).grid(row=4, column=3)

columns = ("Name", "Category", "Amount", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)

tree.grid(row=5, column=0, columnspan=4)

label_total = tk.Label(root, text="Total Expense: RM 0.00", font=("Arial", 12, "bold"))
label_total.grid(row=6, column=0, columnspan=4)

root.mainloop()