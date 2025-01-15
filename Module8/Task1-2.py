import sqlite3

conn = sqlite3.connect('db3.sqlite')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE Students (student_id INTEGER PRIMARY KEY, name Varchar(32), surname Varchar(32), age int, city Varchar(32))')
# cursor.execute('CREATE TABLE Courses (course_id INTEGER PRIMARY KEY, name Varchar(32), time_start timestamp, time_end timestamp)')
# cursor.execute('CREATE TABLE Student_courses (student_id int, course_id int, FOREIGN KEY(course_id) REFERENCES Courses(course_id), FOREIGN KEY(student_id) REFERENCES Students(student_id))')

data_courses = [
    ('Python', '21.07.21', '21.08.21'),
    ('java', '13.07.21', '16.08.21')
]
data_students = [
    ('Max', 'Brooks', 24, 'Spb'),
    ('John', 'Stones', 15, 'Spb'),
    ('Andy', 'Wings', 45, 'Manhester'),
    ('Kate', 'Brooks', 34, 'Spb')
]
data_student_courses = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
]

# cursor.executemany('INSERT INTO Courses (name, time_start, time_end) VALUES (?, ?, ?)', data_courses)
# cursor.executemany('INSERT INTO Students (name, surname, age, city) VALUES (?, ?, ?, ?)', data_students)
# cursor.executemany('INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)', data_student_courses)

conn.commit()

req1 = cursor.execute('SELECT name, surname FROM Students WHERE age > 30')
print(req1.fetchall())

req2 = cursor.execute('SELECT name, surname FROM Students JOIN Student_courses USING(student_id) WHERE course_id == 1')
print(req2.fetchall())

req3 = cursor.execute('''SELECT name, surname, city FROM Students JOIN Student_courses USING(student_id) WHERE course_id == 1 and city == 'Spb' ''')
print(req3.fetchall())
