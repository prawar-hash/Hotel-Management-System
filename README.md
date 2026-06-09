# 🏨 Hotel Management System (Python + MySQL)

A console-based Hotel Management System built using Python and MySQL.  
It manages guest check-ins, room allocation, updates, search, and check-outs with proper room availability tracking.

---

## 🚀 Features

- Add new guest with check-in date  
- View all guests  
- Search guest by ID  
- Update guest room number  
- Check out guest (delete record)  
- View available rooms  
- View occupied rooms  
- Prevent double booking of rooms  

---

## 🛠️ Tech Stack

- Python 3  
- MySQL Database  
- mysql-connector-python  

---

## 🗄️ Database Setup

### Create Database
sql
CREATE DATABASE hotel_db;
Create Table
USE hotel_db;

CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    room_no INT,
    check_in_date DATE
);
---
⚙️ Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/hotel-management-system.git
cd hotel-management-system

3. Install Dependencies
pip install mysql-connector-python

4. Configure Database
Update your MySQL credentials in the Python file:

self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hotel_db"
)
4. Run the Project
python main.py
📌 Menu Options
1. Add Guest
2. View Guests
3. Search Guest
4. Update Guest Room
5. Check Out Guest
6. View Available Rooms
7. View Occupied Rooms
8. Exit
---
📂 Project Structure
hotel-management-system/
│
├── main.py
└── README.md
---
📈 Future Improvements
- Add GUI using Tkinter or PyQt
- Implement login system (admin/staff)
- Add billing and payment system
- Add room booking history
- Improve error handling and logging
---
👨‍💻 Author

Developed as a beginner-friendly Python + MySQL project to understand CRUD operations, database connectivity, and real-world system design.
---
⭐ Support

If you like this project, give it a ⭐ on GitHub.
