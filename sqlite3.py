import sqlite3

# 连接到数据库
conn = sqlite3.connect('students.db')

# 创建学生表
conn.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                grade INTEGER NOT NULL)''')

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))

    # 插入学生记录
    conn.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("Student added successfully!")

def display_students():
    cursor = conn.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found.")
    else:
        print("Student List:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

def search_student():
    name = input("Enter student name to search: ")

    cursor = conn.execute("SELECT * FROM students WHERE name=?", (name,))
    students = cursor.fetchall()

    if len(students) == 0:
        print("No students found with that name.")
    else:
        print("Search Results:")
        for student in students:
            print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# 关闭数据库连接
conn.close()
