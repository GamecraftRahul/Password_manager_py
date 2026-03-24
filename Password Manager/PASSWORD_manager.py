import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector

# ----------------- MySQL Connection -----------------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",                    # ← your MySQL username
        password="RAHUL123", # ← your MySQL password
        database="password_manager"
    )

# Fetch all records
def fetch_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM accounts")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Insert new record
def insert_account(acc_type, acc_name, email, username, password, notes):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO accounts (account_type, account_name, email, username, password, notes)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (acc_type, acc_name, email, username, password, notes))
    conn.commit()
    conn.close()

# ----------------- GUI Setup -----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔐 Password Manager")
app.geometry("1200x650")

# ----------------- Functions -----------------
def load_data():
    table.delete(*table.get_children())
    for row in fetch_accounts():
        table.insert("", "end", values=row)

def add_account():
    acc_type = entry_type.get()
    acc_name = entry_name.get()
    email = entry_email.get()
    username = entry_username.get()
    password = entry_password.get()
    notes = entry_notes.get("1.0", "end")

    if acc_type == "" or acc_name == "" or password == "":
        messagebox.showwarning("Warning", "Account Type, Name, and Password are required!")
        return

    insert_account(acc_type, acc_name, email, username, password, notes)
    messagebox.showinfo("Success", "Account added successfully!")
    load_data()

# ---------------- Left Panel -----------------
left_frame = ctk.CTkFrame(app, width=350, corner_radius=20)
left_frame.pack(side="left", fill="y", padx=20, pady=20)

ctk.CTkLabel(left_frame, text="Add New Account", font=("Helvetica", 28, "bold")).pack(pady=15)

entry_type = ctk.CTkEntry(left_frame, placeholder_text="Account Type (Email / Bank / Social)", font=("Helvetica", 18))
entry_type.pack(pady=10)

entry_name = ctk.CTkEntry(left_frame, placeholder_text="Account Name", font=("Helvetica", 18))
entry_name.pack(pady=10)

entry_email = ctk.CTkEntry(left_frame, placeholder_text="Email ID", font=("Helvetica", 18))
entry_email.pack(pady=10)

entry_username = ctk.CTkEntry(left_frame, placeholder_text="Username", font=("Helvetica", 18))
entry_username.pack(pady=10)

entry_password = ctk.CTkEntry(left_frame, placeholder_text="Password", font=("Helvetica", 18))
entry_password.pack(pady=10)

entry_notes = ctk.CTkTextbox(left_frame, height=120, font=("Helvetica", 18))
entry_notes.pack(pady=10)

ctk.CTkButton(left_frame, text="Add Account", font=("Helvetica", 22, "bold"), height=50, command=add_account).pack(pady=20)

# ---------------- Right Panel (Table) -----------------
right_frame = ctk.CTkFrame(app, corner_radius=20)
right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 18, "bold"))
style.configure("Treeview", rowheight=35, font=("Helvetica", 16))

table = ttk.Treeview(
    right_frame,
    columns=("ID", "Type", "Name", "Email", "Username", "Password", "Notes", "Created"),
    show="headings"
)

headers = ["ID", "Type", "Name", "Email", "Username", "Password", "Notes", "Created"]
for col in headers:
    table.heading(col, text=col)
    table.column(col, width=140)

table.pack(expand=True, fill="both", padx=15, pady=15)

load_data()

app.mainloop()
