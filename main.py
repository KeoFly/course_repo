"""class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = p1 + p2
print(p3)"""
from os.path import abspath

"""class Student:

    tired = 0
    progress = 0

    def __init__(self, name):
        self.name = name
        
    def study(self):
        self.progress += 10
        self.tired += 15
    def relax(self):
        if self.tired > 5:
            self.tired -= 5
        else:
            self.tired = 0
    def is_done(self):
        if self.progress >= 100:
            print("Done")
        else:
            print("Not yet")

s = Student("Ilya")
print(s.name)
"""



"""class Stack:

    def __init__(self, data):
        self.data = data

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.data != []:
            element = self.data[-1]
            del self.data[-1]
            return element

s = Stack([1, 3, 5])

s.push(4)
s.push(7)

for i in range(3):
    print(s.pop())"""


"""class Matrix:

    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])

    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            data1 = []
            for i in range(self.n):
                curr_data = []
                for j in range(self.m):
                    curr_data.append(self.data[i][j] + other.data[i][j])
                data1.append(curr_data)
            return Matrix(data1)
        else:
            return "Wrong dimention"

m1 = Matrix([[1, 2], [1, 2]])
m2 = Matrix([[1, 0], [0, 1]])

m3 = m1 + m2

print(m3.data)"""


"""class Animal:

    def __init__(self, name):
        self.__name = name
        self.health = 100

    def make_noize(self):
        print("Grrrrrrrr")

class Cat(Animal):

    def make_noize(self):
        print("Meow")

class Dog(Animal):

    def make_noize(self):
        print("Gav")

cat1 = Cat("barsik")
dog = Dog("Rex")

dog.make_noize()
cat1.make_noize()

print(cat1._Animal__name)"""



"""class Salary:

    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12

class Employee:

    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(pay)

    def annual_salary(self):
        return self.bonus + self.salary.get_total()

emp = Employee(1000, 1000)

print(emp.annual_salary())"""
print(abspath(__file__))