import sqlite3

# объявление класса Student
class Student:
    def __init__(self, name, surname, father, group, grades):
        self.name = name
        self.surname = surname
        self.father = father
        self.group = group
        self.grades = grades

# создание студента
def make_stud():
    name = input("name ")
    surname = input("surname ")
    father = input("father ")
    group = input("group ")
    grades = [int(input(f"grades ")) for _ in range(4)]
    stud = Student(name, surname, father, group, grades)
    return stud


# создание таблы
con = sqlite3.connect("students.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students
            (id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            father TEXT,
            group_name TEXT,
            grade1 INTEGER,
            grade2 INTEGER,
            grade3 INTEGER,
            grade4 INTEGER)
            """)

# добавление студента
def add_stud(student):
    con = sqlite3.connect('students.db')
    cursor = con.cursor()
    cursor.execute('''
            INSERT INTO students (name, surname, father, group_name, grade1, grade2, grade3, grade4)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (student.name, student.surname, student.father, student.group, *student.grades))
    con.commit()

# просмотр всех студентов
def check_all():
    con = sqlite3.connect('students.db')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM students')
    for i in cursor.fetchall():
        print(i)

# просмотр одного студента
def check_one(id):
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students WHERE id=?", (id, ))
    stud = cursor.fetchone()
    print(stud, sum(stud[5:9]) / 4)

# редактирование студента
def edit_stud(id, student):
    con = sqlite3.connect('students.db')
    cursor = con.cursor()
    cursor.execute('''
            UPDATE students 
            SET name=?, surname=?, father=?, group_name=?, grade1=?, grade2=?, grade3=?, grade4=? WHERE id=?
        ''', (student.name, student.surname, student.father, student.group, *student.grades, id))
    con.commit()

#удаление студента
def del_stud(id):
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM students WHERE id=?", (id, ))
    con.commit()

def average_group(group):
    con = sqlite3.connect("students.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM students WHERE group_name=?", (group, ))
    for i in cursor.fetchall():
        return i[1:4], sum(i[5:9]) / 4

while True:
    comm = input("1 add\n2 check all\n3 check one\n4 edit\n5 del\n6 average group\n- stop\n")
    if comm == "1":
        stud = make_stud()
        add_stud(stud)

    elif comm == "2":
        check_all()

    elif comm == "3":
        id = int(input("id "))
        check_one(id)

    elif comm == "4":
        id = int(input("id "))
        stud = make_stud()
        edit_stud(id, stud)

    elif comm == "5":
        id = int(input("id "))
        del_stud(id)

    elif comm == "6":
        group = input("group ")
        print(average_group(group))

    else:
        break