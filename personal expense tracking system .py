import tkinter as tk
from tkinter import ttk, messagebox
import os
import json
from datetime import datetime

# ==========================================
# CONFIGURATION & STYLES
# ==========================================
COLORS = {
    "bg": "#1e1e2e",          # Deep dark blue/grey
    "fg": "#cdd6f4",          # Off-white text
    "accent": "#89b4fa",      # Blue accent
    "button": "#313244",      # Slightly lighter button bg
    "button_hover": "#45475a",# Hover state
    "success": "#a6e3a1",     # Green
    "error": "#f38ba8",       # Red
    "input_bg": "#11111b"     # Very dark input background
}

FONTS = {
    "header": ("Helvetica", 16, "bold"),
    "normal": ("Helvetica", 10),
    "small": ("Helvetica", 9)
}

DATA_FILE = "expenses.json"

# ==========================================
# DATA HANDLING CLASS (Backend)
# ==========================================
class DataManager:
    def __init__(self, filename):
        self.filename = filename

    def load_data(self):
        """Loads data from JSON file. If file doesn't exist, returns empty list."""
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            # Error handling for corrupted files
            return []

    def save_data(self, data):
        """Saves list of expenses to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except IOError:
            messagebox.showerror("Error", "Failed to save data to file!")
            return False

# ==========================================
# GUI APPLICATION CLASS
# ==========================================
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.data_manager = DataManager(DATA_FILE)
        self.categories = ["Food", "Transport", "Utilities", "Entertainment", "Health", "Shopping", "Other"]
        
        # Setup Window
        self.root.title("Personal Expense Tracker")
        self.root.geometry("900x600")
        self.root.configure(bg=COLORS["bg"])
        
        # Initialize UI
        self.create_widgets()
        self.refresh_expense_list()

    def create_widgets(self):
        """Creates all GUI widgets."""
        
        # --- HEADER SECTION ---
        header_frame = tk.Frame(self.root, bg=COLORS["bg"])
        header_frame.pack(pady=20)
        
        lbl_title = tk.Label(header_frame, text="EXPENSE TRACKER", font=("Helvetica", 24, "bold"), 
                            bg=COLORS["bg"], fg=COLORS["accent"])
        lbl_title.pack()

        # --- INPUT SECTION ---
        input_frame = tk.Frame(self.root, bg=COLORS["bg"])
        input_frame.pack(pady=10, padx=20, fill="x")

        # Grid Layout for Inputs
        # Row 0: Labels
        tk.Label(input_frame, text="Amount ($):", font=FONTS["normal"], bg=COLORS["bg"], fg=COLORS["fg"]).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        tk.Label(input_frame, text="Category:", font=FONTS["normal"], bg=COLORS["bg"], fg=COLORS["fg"]).grid(row=0, column=1, padx=5, pady=5, sticky="e")
        tk.Label(input_frame, text="Description:", font=FONTS["normal"], bg=COLORS["bg"], fg=COLORS["fg"]).grid(row=0, column=2, padx=5, pady=5, sticky="e")
        
        # Row 1: Inputs
        self.entry_amount = self.create_styled_entry(input_frame, width=15)
        self.entry_amount.grid(row=1, column=0, padx=5, pady=5)

        self.combo_category = ttk.Combobox(input_frame, values=self.categories, state="readonly", font=FONTS["normal"])
        self.combo_category.grid(row=1, column=1, padx=5, pady=5)
        self.combo_category.current(0) # Set default

        self.entry_desc = self.create_styled_entry(input_frame, width=30)
        self.entry_desc.grid(row=1, column=2, padx=5, pady=5)

        # --- ACTION BUTTONS ---
        btn_frame = tk.Frame(self.root, bg=COLORS["bg"])
        btn_frame.pack(pady=15)

        self.create_styled_button(btn_frame, "ADD EXPENSE", lambda: self.add_expense()).grid(row=0, column=0, padx=10)
        self.create_styled_button(btn_frame, "VIEW ALL", lambda: self.refresh_expense_list()).grid(row=0, column=1, padx=10)
        self.create_styled_button(btn_frame, "CLEAR INPUTS", lambda: self.clear_inputs()).grid(row=0, column=2, padx=10)

        # --- DATA DISPLAY (Treeview) ---
        tree_frame = tk.Frame(self.root, bg=COLORS["bg"])
        tree_frame.pack(pady=10, padx=20, fill="both", expand=True)

        # Scrollbar
        scroll = ttk.Scrollbar(tree_frame)
        scroll.pack(side="right", fill="y")

        # Columns
        columns = ("date", "category", "amount", "desc")
        self.tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=scroll.set)
        
        # Heading configuration
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("desc", text="Description")

        # Column sizing
        self.tree.column("date", width=100)
        self.tree.column("category", width=120)
        self.tree.column("amount", width=100)
        self.tree.column("desc", width=300)

        self.tree.pack(fill="both", expand=True)
        scroll.config(command=self.tree.yview)

        # Apply custom styles to Treeview
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", 
                      background=COLORS["input_bg"], 
                      foreground=COLORS["fg"], 
                      fieldbackground=COLORS["input_bg"],
                      font=FONTS["normal"])
        style.configure("Treeview.Heading", 
                        background=COLORS["button"], 
                        foreground=COLORS["fg"], 
                        font=("Helvetica", 10, "bold"))
        style.map("Treeview", background=[('selected', COLORS["accent"])])

        # --- FOOTER / STATS ---
        footer_frame = tk.Frame(self.root, bg=COLORS["bg"])
        footer_frame.pack(pady=10, padx=20, fill="x")

        self.lbl_total = tk.Label(footer_frame, text="Total Spent: $0.00", font=("Helvetica", 14, "bold"), 
                                bg=COLORS["bg"], fg=COLORS["success"])
        self.lbl_total.pack(side="right")

    # ==========================================
    # HELPER FUNCTIONS
    # ==========================================
    
    def create_styled_entry(self, parent, width):
        """Creates a styled Entry widget."""
        entry = tk.Entry(parent, width=width, bg=COLORS["input_bg"], fg=COLORS["fg"], 
                         insertbackground=COLORS["fg"], font=FONTS["normal"], relief="flat")
        entry.configure(readonlybackground=COLORS["input_bg"])
        return entry

    def create_styled_button(self, parent, text, command):
        """Creates a custom dark-themed button."""
        btn = tk.Button(parent, text=text, command=command, 
                        bg=COLORS["button"], fg=COLORS["fg"], 
                        activebackground=COLORS["button_hover"], activeforeground=COLORS["accent"],
                        relief="flat", font=("Helvetica", 10, "bold"), cursor="hand2", padx=15, pady=8)
        
        # Bind hover effects manually for better control than standard Tkinter
        btn.bind("<Enter>", lambda e: btn.config(bg=COLORS["button_hover"]))
        btn.bind("<Leave>", lambda e: btn.config(bg=COLORS["button"]))
        
        return btn

    def validate_input(self, amount_str):
        """
        VALIDATION: Uses Conditional logic to check if input is valid.
        Returns float amount if valid, else None.
        """
        if not amount_str.strip():
            return None
        
        try:
            amount = float(amount_str)
            # CONDITIONAL: Check if amount is positive
            if amount <= 0:
                messagebox.showwarning("Warning", "Amount must be greater than 0!")
                return None
            return amount
        except ValueError:
            messagebox.showerror("Error", "InvalidAmount! Please enter a numeric value.")
            return None

    def add_expense(self):
        """Function to add expense using logic and file handling."""
        # INPUT VALIDATION
        amount = self.validate_input(self.entry_amount.get())
        
        if amount is None:
            return # Stop if validation fails
            
        category = self.combo_category.get()
        description = self.entry_desc.get().strip()
        
        if not description:
            description = "No Description" # Default handling

        # Get current date
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Create Data Object (Dictionary)
        new_expense = {
            "date": date_str,
            "category": category,
            "amount": amount,
            "description": description
        }

        # FILE HANDLING: Load, Append, Save
        expenses = self.data_manager.load_data()
        expenses.append(new_expense)
        
        if self.data_manager.save_data(expenses):
            messagebox.showinfo("Success", "Expense added successfully!")
            self.clear_inputs()
            self.refresh_expense_list()
        else:
            messagebox.showerror("Error", "Could not save data.")

    def clear_inputs(self):
        """Clears input fields."""
        self.entry_amount.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)
        self.combo_category.current(0)

    def refresh_expense_list(self):
        """Loads data from file and displays it in the GUI."""
        # Clear current view
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Load Data
        expenses = self.data_manager.load_data()

        total_spent = 0.0

        # LOOPS: Iterate through the list of expenses
        for item in expenses:
            # Display in Treeview
            # Format: [Date, Category, $Amount, Description]
            display_amount = f"${item['amount']:.2f}"
            self.tree.insert("", tk.END, values=(
                item['date'], 
                item['category'], 
                display_amount, 
                item['description']
            ))
            
            # Math Logic for Total
            total_spent += item['amount']

        # Update Total Label
        self.lbl_total.config(text=f"Total Spent: ${total_spent:,.2f}")

# ==========================================
# MAIN ENTRY POINT
# ==========================================
if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()