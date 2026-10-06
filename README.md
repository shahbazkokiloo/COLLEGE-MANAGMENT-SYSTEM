# 🎓 College Management System

A **console-based College Management System built entirely with Python**.
This project is designed to manage students, teachers, courses, attendance, examination results, and fee records through a simple command-line interface.

The system uses **JSON file storage**, so no external database or third-party libraries are required.

---

## 🚀 Features

### 👨‍🎓 Student Management

* Add new students
* View all students
* Search students by ID or name
* Update student information
* Delete student records
* Automatically generated Student IDs

### 👨‍🏫 Teacher Management

* Add teachers
* View teacher records
* Store department and subject information
* Automatically generated Teacher IDs

### 📚 Course Management

* Add courses
* View available courses
* Store course duration and department
* Automatically generated Course IDs

### 📅 Attendance Management

* Mark students as Present or Absent
* View attendance records
* Calculate attendance percentage
* Display total, present, and absent classes

### 📝 Result Management

* Add subject marks
* Calculate percentage automatically
* Generate grades automatically
* View student results
* Calculate average percentage

### 💰 Fee Management

* Add student fee records
* Track Paid/Pending status
* View fee history

### 💾 Data Persistence

All data is automatically stored in:

```text
college_data.json
```

The data remains available even after closing and restarting the program.

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Exception Handling
* Functions
* Classes & Objects
* Lists & Dictionaries
* Date & Time
* Conditional Statements
* Loops

### Python Modules Used

```python
json
os
datetime
```

All of these are part of Python's standard library.

---

## 📂 Project Structure

```text
College-Management-System/
│
├── college_management.py
├── college_data.json
└── README.md
```

> `college_data.json` is automatically created when the program saves data for the first time.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/college-management-system.git
```

### 2. Open the project

```bash
cd college-management-system
```

### 3. Run the program

```bash
python college_management.py
```

On some systems you may need:

```bash
python3 college_management.py
```

---

## 🖥️ Main Menu

When the application starts, you will see:

```text
==================================================
          COLLEGE MANAGEMENT SYSTEM
==================================================

Students  : 0
Teachers  : 0
Courses   : 0
Attendance Records : 0
Results   : 0
Fee Records : 0

==================================================

1. Student Management
2. Teacher Management
3. Course Management
4. Attendance Management
5. Result Management
6. Fee Management
7. Exit
```

---

## 🧑‍💻 Example Student ID

The system automatically generates IDs:

```text
STU001
STU002
STU003
```

Teacher IDs:

```text
TCH001
TCH002
```

Course IDs:

```text
CRS001
CRS002
```

---

## 📊 Grade System

The result module automatically calculates grades based on percentage:

| Percentage    | Grade |
| ------------- | ----- |
| 90% and above | A+    |
| 80% – 89%     | A     |
| 70% – 79%     | B     |
| 60% – 69%     | C     |
| 50% – 59%     | D     |
| Below 50%     | F     |

---

## 🧠 Concepts Practiced

This project was created to practice real-world Python programming concepts such as:

* Object-Oriented Programming
* Classes and Objects
* Methods
* Encapsulation
* Functions
* Loops
* Conditional Logic
* Lists
* Dictionaries
* JSON Data
* File Handling
* Exception Handling
* Searching and Filtering
* Data Validation
* Automatic ID Generation
* Basic CRUD Operations

---

## 🔮 Future Improvements

Possible improvements for future versions:

* [ ] Admin login system
* [ ] Teacher login
* [ ] Student login
* [ ] Password authentication
* [ ] SQLite database
* [ ] Student result report generation
* [ ] PDF report generation
* [ ] Better input validation
* [ ] Subject-wise attendance
* [ ] Semester-wise results
* [ ] GUI using Tkinter
* [ ] REST API using FastAPI
* [ ] Web frontend

---

## 🎯 Purpose

This project was developed as a **Python practice and portfolio project** to understand how Python can be used to build a complete management system with persistent data storage.

It demonstrates how fundamental Python concepts can be combined to create a practical application.

---

## 👨‍💻 Author

**Shahbaz Showkat**

BCA Hons
CASET College of Computer Science
Affiliated with University of Kashmir

### Connect

* GitHub: https://github.com/shahbazkokiloo
* LinkedIn: https://www.linkedin.com/in/shahbaaz-showkat-22547434a
* Email: [shahbazbinshowkat@gmail.com](mailto:shahbazbinshowkat@gmail.com)

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---

### 📜 License

This project is open-source and available for educational and learning purposes.
