from peewee import *

conn = SqliteDatabase('db2.sqlite')

class User(Model):
    first_name = CharField(column_name='first_name')
    last_name = CharField(column_name='last_name')
    age = IntegerField(column_name='age')

    class Meta:
        database = conn

class Products(Model):
    name = CharField(column_name='name')
    category = IntegerField(column_name='category')
    price = IntegerField(column_name='price')

    class Meta:
        database = conn

# User.create_table()
# Products.create_table()

u1 = User(first_name = 'Max', last_name = 'Adams', age = 15)
u1.save()

for user in User.select():
    print(user.first_name, user.age)