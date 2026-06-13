import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import csv, os
from datetime import datetime
import matplotlib.pyplot as plt
from collections import defaultdict
from reportlab.pdfgen import canvas
import platform

FILE = "data.csv"
USER_FILE = "users.csv"

root = tk.Tk()
root.title("ZAI SYSTEM")
root.geometry("1250x750")
root.configure(bg="#0b1220")

logged_user = ""
backup_data = []

# ================= USER =================
def save_user(u, p):
    with open(USER_FILE, "a", newline="") as f:
        csv.writer(f).writerow([u, p])

def user_exists(u):
    if not os.path.exists(USER_FILE):
        return False
    for r in csv.reader(open(USER_FILE)):
        if len(r) >= 2 and r[0] == u:
            return True
    return False

def check_login(u, p):
    if not os.path.exists(USER_FILE):
        return False
    for r in csv.reader(open(USER_FILE)):
        if len(r) >= 2 and r[0] == u and r[1] == p:
            return True
    return False

# ================= SWITCH =================
def show_register():
    login_card.pack_forget()
    register_card.pack(expand=True)

def back_login():
    register_card.pack_forget()
    login_card.pack(expand=True)

# ================= REGISTER =================
def register():
    u = reg_user.get()
    p = reg_pass.get()

    if len(u) == 0 or len(p) == 0:
        messagebox.showerror("Error", "Please fill all fields")
        return

    if len(u) > 15:
        messagebox.showerror("Error", "Username max 15 characters")
        return

    if len(p) < 6:
        messagebox.showerror("Error", "Password min 6 characters")
        return

    if user_exists(u):
        messagebox.showerror("Error", "Username already exists")
        return

    save_user(u, p)
    messagebox.showinfo("Success", "Account created!")
    back_login()

# ================= LOGIN =================
def login():
    global logged_user
    if check_login(user.get(), password.get()):
        logged_user = user.get()
        login_frame.destroy()
        dashboard()
    else:
        messagebox.showerror("Login Failed", "Wrong username or password")

# ================= LOGIN UI =================
login_frame = tk.Frame(root, bg="#0b1220")
login_frame.pack(expand=True, fill="both")

login_card = tk.Frame(login_frame, bg="#111b2e", padx=40, pady=35)
login_card.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_card, text="ZAI FINANCE LOGIN",
         fg="#4cc9f0", bg="#111b2e",
         font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(login_card, text="Username", fg="white", bg="#111b2e").pack(anchor="w")
user = tk.Entry(login_card, width=30)
user.pack(pady=5)

tk.Label(login_card, text="Password", fg="white", bg="#111b2e").pack(anchor="w")
password = tk.Entry(login_card, width=30, show="*")
password.pack(pady=5)

tk.Button(login_card, text="LOGIN", bg="#22c55e",
          fg="white", width=25, command=login).pack(pady=10)

tk.Button(login_card, text="CREATE NEW ACCOUNT",
          bg="#3b82f6", fg="white",
          width=25, command=show_register).pack()

# ================= REGISTER UI (FIXED UX) =================
register_card = tk.Frame(login_frame, bg="#111b2e", padx=40, pady=30)

tk.Label(register_card,
         text="CREATE NEW ACCOUNT",
         fg="#4cc9f0",
         bg="#111b2e",
         font=("Arial", 18, "bold")).pack(pady=10)

form = tk.Frame(register_card, bg="#111b2e")
form.pack(pady=10)

# USERNAME
tk.Label(form, text="Username (max 15 chars):",
         fg="white", bg="#111b2e").grid(row=0, column=0, sticky="w", pady=5)

reg_user = tk.Entry(form, width=30)
reg_user.grid(row=0, column=1, pady=5, padx=10)

# PASSWORD
tk.Label(form, text="Password (min 6 chars):",
         fg="white", bg="#111b2e").grid(row=1, column=0, sticky="w", pady=5)

reg_pass = tk.Entry(form, width=30, show="*")
reg_pass.grid(row=1, column=1, pady=5, padx=10)

# INFO BOX (CLEAR EXPLANATION)
info = tk.Label(register_card,
         text="✔ Username: max 15 characters (letters/numbers/symbols)\n"
              "✔ Password: minimum 6 characters\n"
              "✔ Must remember for login",
         fg="#cbd5e1", bg="#111b2e", justify="left")
info.pack(pady=10)

btns = tk.Frame(register_card, bg="#111b2e")
btns.pack(pady=10)

tk.Button(btns, text="CREATE ACCOUNT",
          bg="#22c55e", fg="white",
          width=20, command=register).grid(row=0, column=0, padx=5)

tk.Button(btns, text="BACK",
          bg="#6b7280", fg="white",
          width=20, command=back_login).grid(row=0, column=1, padx=5)

register_card.pack_forget()

# ================= VALIDATION (NUMBERS ONLY) =================

def only_number(char):
    return char.isdigit() or char == ""

validate_cmd = root.register(only_number)

# ================= DASHBOARD =================
def dashboard():

    global tree, total_label, backup_data

    backup_data = []  # FIX: initialize backup

    category = tk.StringVar(value="Select Category")
    rm = tk.StringVar()
    sen = tk.StringVar()
    desc = tk.StringVar()
    search = tk.StringVar()
    search_cat = tk.StringVar()
    salary_var = tk.StringVar()

    # ================= VALIDATION DIGIT =================
    def validate_input(char):
        return char.isdigit() or char == ""

    validate_cmd = root.register(validate_input)

    # ================= BACKUP =================
    def backup():
        global backup_data
        backup_data = [tree.item(i)["values"] for i in tree.get_children()]

    def undo():
        if not backup_data:
            return
        tree.delete(*tree.get_children())
        for r in backup_data:
            tree.insert("", "end", values=r)

    # ================= SAVE =================
    def save():
        with open(FILE, "w", newline="") as f:
            w = csv.writer(f)
            for i in tree.get_children():
             values = tree.item(i)["values"]

             if values[0] == "TOTAL" or values[0] == "":
               continue
            w.writerow(values)

    # ================= LOAD =================
    def load():
        if not os.path.exists(FILE):
            return
        for r in csv.reader(open(FILE)):
            if len(r) >= 5:
                tree.insert("", "end", values=r)

    # ================= ADD =================
    def add():
        backup()

        if category.get() == "Select Category":
            messagebox.showerror("Error", "Please select category")
            return

        if not rm.get() and not sen.get():
            messagebox.showerror("Error", "Please enter amount")
            return

        try:
            amount = float(rm.get() or 0) + float(sen.get() or 0) / 100
        except:
            messagebox.showerror("Error", "Invalid amount")
            return

        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than 0")
            return

        d = date.get_date()

        tree.insert("", "end", values=(
            d.strftime("%Y-%m-%d"),
            d.strftime("%A"),
            category.get(),
            f"RM {amount:.2f}",
            desc.get()
        ))

        save()
        total()
        finance_status()

        category.set("Select Category")
        rm.set("")
        sen.set("")
        desc.set("")
        date.set_date(datetime.now())

    # ================= DELETE =================
    def delete():
        backup()
        for i in tree.selection():
            tree.delete(i)
        save()
        total()
        finance_status()

    # ================= CLEAR =================
    def clear():
        backup()
        tree.delete(*tree.get_children())
        save()
        total()
        finance_status()

    def total():
     t = 0

        # Buang TOTAL lama dan row kosong lama
     for item in tree.get_children():
            values = tree.item(item)["values"]

            if len(values) > 0:
                if values[0] == "TOTAL" or values[0] == "":
                    tree.delete(item)

        # Kira jumlah
     for item in tree.get_children():
            values = tree.item(item)["values"]

            try:
                t += float(str(values[3]).replace("RM", "").strip())
            except:
                pass

     total_label.config(text=f"Total Spending: RM {t:.2f}")

     # Jarak 2 baris
     tree.insert("", "end", values=("", "", "", "", ""))
     tree.insert("", "end", values=("", "", "", "", ""))

    # Row TOTAL
     tree.insert(
            "",
            "end",
            values=("TOTAL", "", "", f"RM {t:.2f}", ""),
            tags=("total_row",)
        )

    # ================= FINANCE STATUS =================
    def finance_status():
        try:
            salary = float(salary_var.get())
        except:
            salary = 0

        spent = sum(float(tree.item(i)["values"][3].replace("RM", "")) for i in tree.get_children())
        balance = salary - spent

        if salary == 0:
            status = "Enter salary first"
        elif balance < 0:
            status = "⚠ OVERSPENDING"
        elif balance < salary * 0.3:
            status = "⚠ HIGH SPENDING"
        else:
            status = "✅ HEALTHY"

        status_label.config(text=f"{status} | Balance: RM {balance:.2f}")

    # ================= SEARCH =================
    def search_data():
        q = search.get().lower()
        cat = search_cat.get()
        dfilter = cal.get_date().strftime("%Y-%m-%d") if cal_used.get() else None

        tree.delete(*tree.get_children())

        for r in csv.reader(open(FILE)):
            if len(r) < 5:
                continue

            ok = True

            if q and q not in str(r).lower():
                ok = False

            if cat and cat != "Select Category":
                if cat.lower() not in r[2].lower():
                    ok = False

            if dfilter and dfilter not in r[0]:
                ok = False

            if ok:
                tree.insert("", "end", values=r)

    # ================= LOAD ALL =================
    def load_all():
        tree.delete(*tree.get_children())

        if os.path.exists(FILE):
            for r in csv.reader(open(FILE)):
                if len(r) >= 5:
                    tree.insert("", "end", values=r)

        search.set("")
        search_cat.set("Select Category")
        cal_used.set(0)

    # ================= CHART =================
    def chart():
        data = defaultdict(float)

        for i in tree.get_children():
            r = tree.item(i)["values"]
            data[r[2]] += float(r[3].replace("RM", ""))

        plt.figure()
        plt.title("Spending Breakdown")
        plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
        plt.show()

    # ================= PDF =================
    def pdf():
        file = f"{logged_user}_report.pdf"
        c = canvas.Canvas(file)

        c.setFont("Helvetica-Bold", 16)
        c.drawString(180, 800, "FINANCE REPORT")

        c.setFont("Helvetica", 10)
        c.drawString(50, 780, f"User: {logged_user}")
        c.drawString(50, 765, f"Generated: {datetime.now()}")

        c.line(50, 755, 550, 755)

        y = 730
        c.setFont("Helvetica-Bold", 10)
        c.drawString(50, y, "Date")
        c.drawString(130, y, "Day")
        c.drawString(200, y, "Category")
        c.drawString(300, y, "Amount")
        c.drawString(400, y, "Description")

        y -= 20
        c.setFont("Helvetica", 9)
        
        for i in tree.get_children():
            r = tree.item(i)["values"]


            c.drawString(50, y, str(r[0]))
            c.drawString(130, y, str(r[1]))
            c.drawString(200, y, str(r[2]))
            c.drawString(300, y, str(r[3]))
            c.drawString(400, y, str(r[4])[:25])

            y -= 18

            if y < 50:
                c.showPage()
                y = 750
            c.line(50, y - 5, 550, y - 5)

        c.save()
        messagebox.showinfo("PDF", "Report generated!")

        if platform.system() == "Windows":
            os.startfile(file)

    # ================= UI =================
    main = tk.Frame(root, bg="#0b1220")
    main.pack(fill="both", expand=True)

    # LEFT PANEL
    left = tk.Frame(main, bg="#111b2e", padx=20, pady=20)
    left.pack(side="left", fill="y")

    tk.Label(left, text=f"USER: {logged_user}",
             fg="#4cc9f0", bg="#111b2e",
             font=("Arial", 12, "bold")).pack()

    tk.Label(left, text="Monthly Salary", fg="white", bg="#111b2e").pack(anchor="w")
    tk.Entry(left, textvariable=salary_var).pack(fill="x")

    tk.Button(left, text="CHECK STATUS",
              bg="#3b82f6", fg="white",
              command=finance_status).pack(fill="x", pady=5)

    status_label = tk.Label(left, text="Status: -",
                            fg="#facc15", bg="#111b2e",
                            wraplength=200)
    status_label.pack()

    # FORM
    form = tk.Frame(left, bg="#0f172a", padx=10, pady=10)
    form.pack(fill="x", pady=10)

    tk.Label(form, text="Category", fg="white", bg="#0f172a").pack(anchor="w")

    cat_box = ttk.Combobox(
        form,
        textvariable=category,
        values=["Select Category","Food","Transport","Bills","Shopping","Utilities","Entertainment","Health","Other"],
        state="readonly"
    )
    cat_box.pack(fill="x")
    cat_box.set("Select Category")

    tk.Label(form, text="Date", fg="white", bg="#0f172a").pack(anchor="w")

    date = DateEntry(form,date_pattern="yyyy-mm-dd",state="readonly")
    date.pack(fill="x")

    # 🔥 block typing sahaja (TIDAK ganggu calendar)
    def block_typing(event):
        if event.keysym not in ("Down", "Up", "Return"):
            return "break"

    date.bind("<Key>", block_typing)

    tk.Label(form, text="Amount", fg="white", bg="#0f172a").pack(anchor="w")

    amt_frame = tk.Frame(form, bg="#0f172a")
    amt_frame.pack(fill="x")

    tk.Label(amt_frame, text="RM", fg="white", bg="#0f172a").pack(side="left")
    tk.Entry(amt_frame, textvariable=rm, width=10,
             validate="key", validatecommand=(validate_cmd, "%S")).pack(side="left")

    tk.Label(amt_frame, text="SEN", fg="white", bg="#0f172a").pack(side="left")
    tk.Entry(amt_frame, textvariable=sen, width=5,
             validate="key", validatecommand=(validate_cmd, "%S")).pack(side="left", padx=5)

    tk.Label(form, text="Description", fg="white", bg="#0f172a").pack(anchor="w")
    tk.Entry(form, textvariable=desc).pack(fill="x")

    tk.Button(left, text="➕ ADD", bg="#22c55e", command=add).pack(fill="x", pady=5)
    tk.Button(left, text="↩ UNDO", bg="#f59e0b", command=undo).pack(fill="x", pady=5)
    tk.Button(left, text="🗑 CLEAR", bg="#ef4444", command=clear).pack(fill="x", pady=5)

    # RIGHT PANEL
    right = tk.Frame(main, bg="#0b1220")
    right.pack(side="right", fill="both", expand=True)

    topbar = tk.Frame(right, bg="#111b2e", padx=10, pady=10)
    topbar.pack(fill="x")


    tk.Entry(topbar, textvariable=search, width=20).pack(side="left")

    search_cat.set("")
    search_cat = tk.StringVar()

    search_cat_box = ttk.Combobox(
        topbar,
        textvariable=search_cat,
        values=["Select Category","Food","Transport","Bills","Shopping","Utilities","Entertainment","Health","Other"],
        state="readonly"   # 🔥 INI YANG KUNCI
    )

    search_cat_box.pack(side="left", padx=5)
    search_cat_box.set("Select Category")

    cal_used = tk.IntVar()
    tk.Checkbutton(topbar, text="Date Filter",
                   variable=cal_used,
                   fg="white", bg="#111b2e").pack(side="left")

    cal = DateEntry(topbar,state='readonly',date_pattern="yyyy-mm-dd")
    date.pack(fill="x")
    
    cal.pack(side="left", padx=5)

    tk.Button(topbar, text="SEARCH", bg="#3b82f6",
              fg="white", command=search_data).pack(side="left")
    
    tk.Button(topbar, text="VIEW ALL", bg="#f59e0b",
              fg="white", command=load_all).pack(side="left", padx=5)
    
    tk.Button(topbar, text="CHART", bg="#8b5cf6",
              fg="white", command=chart).pack(side="right", padx=5)

    tk.Button(topbar, text="PDF", bg="#10b981",
              fg="white", command=pdf).pack(side="right", padx=5)

    tk.Button(topbar, text="DELETE", bg="#ef4444",
              fg="white", command=delete).pack(side="right", padx=5)

    # TABLE
    tree = ttk.Treeview(right,
                        columns=("Date","Day","Category","Amount","Description"),
                        show="headings")
    tree.pack(fill="both", expand=True)

    tree.tag_configure(
    "total_row",
    background="#facc15",
    font=("Arial", 10, "bold")
    )

    style = ttk.Style()

    style.configure(
        "Treeview",
        rowheight=30,
        borderwidth=1,
        relief="solid"
    )

    style.configure(
        "Treeview.Heading",
        relief="raised",
        borderwidth=1
    )

    for c in tree["columns"]:
        tree.heading(c, text=c)
        tree.column(c, anchor="center", width=130)

    total_label = tk.Label(right,
                           text="Total: RM 0.00",
                           fg="#facc15",
                           bg="#0b1220",
                           font=("Arial", 12, "bold"))
    total_label.pack()

    load()
    total()
    finance_status()

root.mainloop()