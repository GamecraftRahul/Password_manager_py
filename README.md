# 🔐 Password Manager

A modern desktop-based **Password Manager** developed using **Python**, **CustomTkinter**, and **MySQL**. The application allows users to securely organize login credentials for multiple accounts such as email, banking, social media, and other online services through an intuitive graphical interface.

---

## 📌 Features

- 🔐 Store passwords securely in a MySQL database
- 👤 Save account information
- 📧 Store email addresses
- 🆔 Save usernames
- 📝 Add custom notes for each account
- 📂 Organize accounts by category
- 📋 Display all saved accounts in a table
- 🎨 Modern CustomTkinter interface
- 💾 Persistent MySQL database storage

---

## 🖼️ Application Overview

The application provides:

- Left panel for adding new account credentials
- Right panel displaying all saved accounts
- Simple and user-friendly interface
- Fast database connectivity

---

## 🛠️ Technologies Used

- Python 3.x
- CustomTkinter
- Tkinter (TTK)
- MySQL
- mysql-connector-python

---

## 📂 Project Structure

```
Password_manager_py-main/
│
├── README.md
│
└── Password Manager/
    ├── PASSWORD_manager.py
    └── Password manager.sql
```

---

## ⚙️ Requirements

- Python 3.10 or later
- MySQL Server
- pip

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Password_manager_py.git
```

### 2. Navigate to the project

```bash
cd Password_manager_py-main
```

### 3. Install dependencies

```bash
pip install customtkinter
pip install mysql-connector-python
```

Or install everything together:

```bash
pip install customtkinter mysql-connector-python
```

---

## 🗄️ Database Setup

### Create the database

```sql
CREATE DATABASE password_manager;
```

### Import the SQL file

Import:

```
Password manager.sql
```

using MySQL Workbench, phpMyAdmin, or the MySQL command line.

---

## ⚙️ Configure Database

Open **PASSWORD_manager.py** and update the connection details if necessary.

```python
host="localhost"
user="root"
password="YOUR_PASSWORD"
database="password_manager"
```

---

## ▶️ Running the Project

```bash
cd "Password Manager"

python PASSWORD_manager.py
```

---

## 📊 Database Fields

The application stores:

- Account ID
- Account Type
- Account Name
- Email Address
- Username
- Password
- Notes
- Created Date

---

## 📦 Dependencies

- customtkinter
- mysql-connector-python
- tkinter (included with Python)

---

## 🚀 Future Enhancements

- 🔒 Master password authentication
- 🔑 Password encryption (AES/Fernet)
- 👁️ Show/Hide password toggle
- 🔍 Search accounts
- ✏️ Edit existing records
- ❌ Delete records
- 📋 Copy password to clipboard
- 🔐 Password generator
- 📤 Export passwords
- ☁️ Cloud synchronization
- 🌙 Light/Dark mode switch
- 🔄 Backup & Restore database

---

## 👨‍💻 Author

**Rahul Kulkarni**


---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is developed for educational and learning purposes.

Feel free to modify and enhance it according to your requirements.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
