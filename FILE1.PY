
import json
import os
from datetime import datetime


DATA_FILE = "college_data.json"


class CollegeManagementSystem:

    def __init__(self):
        self.data = {
            "students": [],
            "teachers": [],
            "courses": [],
            "attendance": [],
            "results": [],
            "fees": []
        }

        self.load_data()

    # ---------------- DATA MANAGEMENT ---------------- #

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as file:
                    self.data = json.load(file)
            except (json.JSONDecodeError, OSError):
                print("Could not load data. Starting with empty database.")

    def save_data(self):
        try:
            with open(DATA_FILE, "w") as file:
                json.dump(self.data, file, indent=4)

        except OSError:
            print("Error saving data.")

    # ---------------- UTILITY FUNCTIONS ---------------- #

    def generate_id(self, prefix, collection):
        numbers = []

        for item in collection:
            try:
                numbers.append(int(item["id"].replace(prefix, "")))
            except (ValueError, KeyError):
                pass

        next_number = max(numbers, default=0) + 1
        return f"{prefix}{next_number:03d}"

    def find_by_id(self, collection, item_id):
        for item in collection:
            if item["id"].lower() == item_id.lower():
                return item

        return None

    # ---------------- STUDENT MANAGEMENT ---------------- #

    def add_student(self):
        print("\n===== ADD STUDENT =====")

        name = input("Student Name: ").strip()
        age = input("Age: ").strip()
        gender = input("Gender: ").strip()
        course = input("Course: ").strip()
        semester = input("Semester: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()

        student_id = self.generate_id("STU", self.data["students"])

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "course": course,
            "semester": semester,
            "phone": phone,
            "email": email,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.data["students"].append(student)
        self.save_data()

        print(f"\nStudent added successfully!")
        print(f"Student ID: {student_id}")

    def view_students(self):
        print("\n===== ALL STUDENTS =====")

        students = self.data["students"]

        if not students:
            print("No students found.")
            return

        for student in students:
            print("-" * 50)
            print(f"ID       : {student['id']}")
            print(f"Name     : {student['name']}")
            print(f"Age      : {student['age']}")
            print(f"Gender   : {student['gender']}")
            print(f"Course   : {student['course']}")
            print(f"Semester : {student['semester']}")
            print(f"Phone    : {student['phone']}")
            print(f"Email    : {student['email']}")

    def search_student(self):
        print("\n===== SEARCH STUDENT =====")

        keyword = input("Enter Student ID or Name: ").strip().lower()

        results = []

        for student in self.data["students"]:
            if (
                keyword in student["id"].lower()
                or keyword in student["name"].lower()
            ):
                results.append(student)

        if not results:
            print("Student not found.")
            return

        for student in results:
            print("-" * 50)
            print(f"ID       : {student['id']}")
            print(f"Name     : {student['name']}")
            print(f"Course   : {student['course']}")
            print(f"Semester : {student['semester']}")
            print(f"Phone    : {student['phone']}")

    def update_student(self):
        print("\n===== UPDATE STUDENT =====")

        student_id = input("Enter Student ID: ").strip()

        student = self.find_by_id(
            self.data["students"],
            student_id
        )

        if not student:
            print("Student not found.")
            return

        print("Press Enter to keep existing value.")

        name = input(f"Name [{student['name']}]: ").strip()
        course = input(f"Course [{student['course']}]: ").strip()
        semester = input(f"Semester [{student['semester']}]: ").strip()
        phone = input(f"Phone [{student['phone']}]: ").strip()
        email = input(f"Email [{student['email']}]: ").strip()

        if name:
            student["name"] = name

        if course:
            student["course"] = course

        if semester:
            student["semester"] = semester

        if phone:
            student["phone"] = phone

        if email:
            student["email"] = email

        self.save_data()

        print("Student updated successfully.")

    def delete_student(self):
        print("\n===== DELETE STUDENT =====")

        student_id = input("Enter Student ID: ").strip()

        student = self.find_by_id(
            self.data["students"],
            student_id
        )

        if not student:
            print("Student not found.")
            return

        confirmation = input(
            f"Delete {student['name']}? (y/n): "
        ).lower()

        if confirmation == "y":
            self.data["students"].remove(student)
            self.save_data()
            print("Student deleted successfully.")
        else:
            print("Operation cancelled.")

    # ---------------- TEACHER MANAGEMENT ---------------- #

    def add_teacher(self):
        print("\n===== ADD TEACHER =====")

        name = input("Teacher Name: ").strip()
        department = input("Department: ").strip()
        subject = input("Subject: ").strip()
        phone = input("Phone: ").strip()
        email = input("Email: ").strip()

        teacher_id = self.generate_id(
            "TCH",
            self.data["teachers"]
        )

        teacher = {
            "id": teacher_id,
            "name": name,
            "department": department,
            "subject": subject,
            "phone": phone,
            "email": email
        }

        self.data["teachers"].append(teacher)
        self.save_data()

        print(f"\nTeacher added successfully!")
        print(f"Teacher ID: {teacher_id}")

    def view_teachers(self):
        print("\n===== ALL TEACHERS =====")

        if not self.data["teachers"]:
            print("No teachers found.")
            return

        for teacher in self.data["teachers"]:
            print("-" * 50)
            print(f"ID         : {teacher['id']}")
            print(f"Name       : {teacher['name']}")
            print(f"Department : {teacher['department']}")
            print(f"Subject    : {teacher['subject']}")
            print(f"Phone      : {teacher['phone']}")
            print(f"Email      : {teacher['email']}")

    # ---------------- COURSE MANAGEMENT ---------------- #

    def add_course(self):
        print("\n===== ADD COURSE =====")

        name = input("Course Name: ").strip()
        duration = input("Duration: ").strip()
        department = input("Department: ").strip()

        course_id = self.generate_id(
            "CRS",
            self.data["courses"]
        )

        course = {
            "id": course_id,
            "name": name,
            "duration": duration,
            "department": department
        }

        self.data["courses"].append(course)
        self.save_data()

        print(f"\nCourse added successfully!")
        print(f"Course ID: {course_id}")

    def view_courses(self):
        print("\n===== ALL COURSES =====")

        if not self.data["courses"]:
            print("No courses found.")
            return

        for course in self.data["courses"]:
            print("-" * 50)
            print(f"ID         : {course['id']}")
            print(f"Name       : {course['name']}")
            print(f"Duration   : {course['duration']}")
            print(f"Department : {course['department']}")

    # ---------------- ATTENDANCE ---------------- #

    def mark_attendance(self):
        print("\n===== MARK ATTENDANCE =====")

        student_id = input("Student ID: ").strip()

        student = self.find_by_id(
            self.data["students"],
            student_id
        )

        if not student:
            print("Student not found.")
            return

        status = input("Present or Absent (P/A): ").strip().upper()

        if status not in ["P", "A"]:
            print("Invalid attendance status.")
            return

        record = {
            "student_id": student_id.upper(),
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": "Present" if status == "P" else "Absent"
        }

        self.data["attendance"].append(record)
        self.save_data()

        print("Attendance marked successfully.")

    def view_attendance(self):
        print("\n===== ATTENDANCE =====")

        student_id = input("Student ID: ").strip()

        records = [
            record
            for record in self.data["attendance"]
            if record["student_id"].lower() == student_id.lower()
        ]

        if not records:
            print("No attendance records found.")
            return

        present = sum(
            1 for record in records
            if record["status"] == "Present"
        )

        total = len(records)

        percentage = (present / total) * 100

        print(f"\nTotal Classes : {total}")
        print(f"Present       : {present}")
        print(f"Absent        : {total - present}")
        print(f"Attendance    : {percentage:.2f}%")

        print("\nRecords:")

        for record in records:
            print(
                f"{record['date']} - {record['status']}"
            )

    # ---------------- RESULTS ---------------- #

    def add_result(self):
        print("\n===== ADD RESULT =====")

        student_id = input("Student ID: ").strip()

        student = self.find_by_id(
            self.data["students"],
            student_id
        )

        if not student:
            print("Student not found.")
            return

        subject = input("Subject: ").strip()

        try:
            marks = float(input("Marks: "))
            total_marks = float(input("Total Marks: "))
        except ValueError:
            print("Marks must be numbers.")
            return

        if total_marks <= 0:
            print("Invalid total marks.")
            return

        percentage = (marks / total_marks) * 100

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        result = {
            "student_id": student_id.upper(),
            "subject": subject,
            "marks": marks,
            "total_marks": total_marks,
            "percentage": round(percentage, 2),
            "grade": grade
        }

        self.data["results"].append(result)
        self.save_data()

        print("\nResult added successfully.")
        print(f"Percentage : {percentage:.2f}%")
        print(f"Grade      : {grade}")

    def view_result(self):
        print("\n===== STUDENT RESULT =====")

        student_id = input("Student ID: ").strip()

        records = [
            result
            for result in self.data["results"]
            if result["student_id"].lower() == student_id.lower()
        ]

        if not records:
            print("No results found.")
            return

        total_percentage = 0

        print()

        for result in records:
            print("-" * 40)
            print(f"Subject    : {result['subject']}")
            print(
                f"Marks      : "
                f"{result['marks']}/{result['total_marks']}"
            )
            print(f"Percentage : {result['percentage']}%")
            print(f"Grade      : {result['grade']}")

            total_percentage += result["percentage"]

        average = total_percentage / len(records)

        print("-" * 40)
        print(f"Average Percentage: {average:.2f}%")

    # ---------------- FEES ---------------- #

    def add_fee(self):
        print("\n===== FEE MANAGEMENT =====")

        student_id = input("Student ID: ").strip()

        student = self.find_by_id(
            self.data["students"],
            student_id
        )

        if not student:
            print("Student not found.")
            return

        try:
            amount = float(input("Fee Amount: "))
        except ValueError:
            print("Amount must be a number.")
            return

        status = input("Status (Paid/Pending): ").strip().title()

        if status not in ["Paid", "Pending"]:
            print("Invalid status.")
            return

        fee = {
            "student_id": student_id.upper(),
            "amount": amount,
            "status": status,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.data["fees"].append(fee)
        self.save_data()

        print("Fee record added successfully.")

    def view_fees(self):
        print("\n===== FEE RECORDS =====")

        student_id = input("Student ID: ").strip()

        records = [
            fee
            for fee in self.data["fees"]
            if fee["student_id"].lower() == student_id.lower()
        ]

        if not records:
            print("No fee records found.")
            return

        for fee in records:
            print("-" * 40)
            print(f"Amount : ₹{fee['amount']}")
            print(f"Status : {fee['status']}")
            print(f"Date   : {fee['date']}")

    # ---------------- REPORT ---------------- #

    def dashboard(self):
        print("\n" + "=" * 50)
        print("          COLLEGE MANAGEMENT SYSTEM")
        print("=" * 50)

        print(f"Students  : {len(self.data['students'])}")
        print(f"Teachers  : {len(self.data['teachers'])}")
        print(f"Courses   : {len(self.data['courses'])}")
        print(f"Attendance Records : {len(self.data['attendance'])}")
        print(f"Results   : {len(self.data['results'])}")
        print(f"Fee Records : {len(self.data['fees'])}")

        print("=" * 50)

    # ---------------- MENUS ---------------- #

    def student_menu(self):
        while True:
            print("""
===== STUDENT MANAGEMENT =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                break
            else:
                print("Invalid choice.")

    def teacher_menu(self):
        while True:
            print("""
===== TEACHER MANAGEMENT =====

1. Add Teacher
2. View Teachers
3. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_teacher()
            elif choice == "2":
                self.view_teachers()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def course_menu(self):
        while True:
            print("""
===== COURSE MANAGEMENT =====

1. Add Course
2. View Courses
3. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_course()
            elif choice == "2":
                self.view_courses()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def attendance_menu(self):
        while True:
            print("""
===== ATTENDANCE MANAGEMENT =====

1. Mark Attendance
2. View Attendance
3. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.mark_attendance()
            elif choice == "2":
                self.view_attendance()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def result_menu(self):
        while True:
            print("""
===== RESULT MANAGEMENT =====

1. Add Result
2. View Result
3. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_result()
            elif choice == "2":
                self.view_result()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    def fee_menu(self):
        while True:
            print("""
===== FEE MANAGEMENT =====

1. Add Fee Record
2. View Fee Record
3. Back
""")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.add_fee()
            elif choice == "2":
                self.view_fees()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    # ---------------- MAIN MENU ---------------- #

    def run(self):

        while True:

            self.dashboard()

            print("""
1. Student Management
2. Teacher Management
3. Course Management
4. Attendance Management
5. Result Management
6. Fee Management
7. Exit
""")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.student_menu()

            elif choice == "2":
                self.teacher_menu()

            elif choice == "3":
                self.course_menu()

            elif choice == "4":
                self.attendance_menu()

            elif choice == "5":
                self.result_menu()

            elif choice == "6":
                self.fee_menu()

            elif choice == "7":
                print("\nThank you for using College Management System!")
                break

            else:
                print("Invalid choice. Please try again.")


# ---------------- PROGRAM START ---------------- #

if __name__ == "__main__":
    system = CollegeManagementSystem()
    system.run()