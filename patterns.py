"""import sqlite3

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass = Singleton):
    connection = None

    def connect(self):
        if self. connection is None:
            self.connection = sqlite3.connect("db.sqlite")
            self.cursor = self.connection.cursor()
        return self.cursor"""


"""from abc import abstractmethod

class Base:

    @abstractmethod
    def send(self):
        pass

    @abstractmethod
    def info(self):
        pass

class Sender(Base):

    def send(self):
        print('Send to email')

    def info(self):
        print('Some info')

class Decorator(Base):

    def __init__(self, base):
        self.base = base

    def send(self):
        self.base.send()

    def info(self):
        self.base.info()

class VkSender(Decorator):

    def send(self):
        print('Send to vk')


class TelegramSender(Decorator):

    def send(self):
        print('Send to telegram')


s = Sender()
s.send()
s.info()

s1 = VkSender(s)
s2 = TelegramSender(s)
s1.send()
s1.info()
s2.send()
s2.info()"""



"""def outer(func):
    def inner():
        print('===***')
        func()
        print('===***')
    return inner

@outer
def myfunc():
    print("this is my favorite func!")

myfunc()"""


"""import time

def time_check(func):
    def inner():
        start = time.perf_counter()
        func()
        end = time.perf_counter()
        result = end - start
        print(f"Time: {result} ms")
    return inner

@time_check
def first():
    return 9000 ** 900000

@time_check
def second():
    return 5000 ** 2000000

first()
second()"""