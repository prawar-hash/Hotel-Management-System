# 🏨 Hotel Management System

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A **console-based Hotel Management System** built using **Python and MySQL**.  
It helps manage hotel operations such as guest check-in, room allocation, search, update, and check-out in an efficient and structured way.

---

## 📸 Screenshots

### 🖥️ Main Menu

===== HOTEL MANAGEMENT SYSTEM =====

Add Guest
View Guests
Search Guest
Update Guest Room
Check Out Guest
View Available Rooms
View Occupied Rooms
Exit

### 👤 Guest Records Output

----- Guest Records -----
Guest ID : 1
Name : Rahul
Age : 25
Room No : 101
Check In : 2026-06-10


### 🏨 Room Availability

Available Rooms:
102
103
105
108


---

## 🚀 Features

- 👤 Add new guest with check-in date
- 📋 View all guest records
- 🔍 Search guest by ID
- 🔄 Update guest room with occupancy validation
- 🚪 Check-out (delete) guest
- 🏨 View available rooms
- 🛏️ View occupied rooms
- ❌ Prevents double room booking

---

## 🛠️ Tech Stack

- Python 3
- MySQL Database
- mysql-connector-python

---

## 🗄️ Database Setup

### 1. Create Database
```sql
CREATE DATABASE hotel_db;
2. Create Table
USE hotel_db;

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    room_no INT,
    check_in_date DATE
);
⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/hotel-management-system.git
cd hotel-management-system
2. Install Dependencies
pip install mysql-connector-python
3. Configure Database Connection

Update credentials in Python file:

self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hotel_db"
)
4. Run the Application
python main.py
📌 System Menu
1. Add Guest
2. View Guests
3. Search Guest
4. Update Guest Room
5. Check Out Guest
6. View Available Rooms
7. View Occupied Rooms
8. Exit
📂 Project Structure
hotel-management-system/
│
├── main.py
├── README.md
└── database.sql (optional)
🔐 Security Note

⚠️ Do not hardcode production database credentials.
Use environment variables for better security.

📈 Future Improvements
🖥️ GUI using Tkinter / PyQt
🔐 Admin login system
💰 Billing & payment module
📊 Dashboard analytics
🌐 Web-based version (Flask/Django)
👨‍💻 Author

Hotel Management System Project
Built for learning Python + MySQL integration and CRUD operations.

⭐ Show Your Support

If you like this project:

⭐ Star the repository
🍴 Fork it
🛠️ Improve it
