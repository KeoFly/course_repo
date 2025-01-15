from peewee import *

conn = SqliteDatabase('db4.sqlite')
cursor = conn.cursor()

class Students(Model):
    student_id = PrimaryKeyField(column_name='student_id')
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn

class Courses(Model):
    course_id = PrimaryKeyField(column_name='course_id')
    name = CharField(column_name='course_name')
    time_start = TimeField(column_name='time_start')
    time_end = TimeField(column_name='time_end')

    class Meta:
        database = conn

class StudentCourse(Model):
    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

    class Meta:
        database = conn

Students.drop_table()
Courses.drop_table()
StudentCourse.drop_table()

Students.create_table()
Courses.create_table()
StudentCourse.create_table()

data_students = [
    ('Max', 'Brooks', 24, 'Spb'),
    ('John', 'Stones', 15, 'Spb'),
    ('Andy', 'Wings', 45, 'Manhester'),
    ('Kate', 'Brooks', 34, 'Spb')
]
data_courses = [
    ('Python', '21.07.21', '21.08.21'),
    ('java', '13.07.21', '16.08.21')
]
data_student_courses = [
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2)
]

Students.insert_many(data_students).execute()
Courses.insert_many(data_courses).execute()
StudentCourse.insert_many(data_student_courses).execute()

for student in Students.select().where(Students.age > 30):
    print(student.name)

for student in Students.select().join(StudentCourse).where(StudentCourse.course_id == 1):
    print(student.name, student.surname)

for student in Students.select().join(StudentCourse).where(StudentCourse.course_id == 1).where(Students.city == 'Spb'):
    print(student.name, student.surname, StudentCourse.course_id)