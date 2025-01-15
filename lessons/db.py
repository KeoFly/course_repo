import sqlite3
from datetime import datetime

conn = sqlite3.connect('db1.sqlite')

cursor = conn.cursor()

#cursor.execute('CREATE TABLE Users (firstname Varchar(32), lastname Varchar(32), age int)')

# cursor.execute('''INSERT INTO Users (firstname, lastname, age) VALUES ('Max', 'Adams', '15')''')

# cursor.executemany('INSERT INTO Users VALUES (?, ?, ?)', [('Alex', 'Smith', 44),
#                                                                                 ('John', 'Brooks', 11)])

# cursor.execute('SELECT * FROM Users')

# print(cursor.fetchall())


# cursor.execute('CREATE TABLE Products (name Varchar(32), category int, price int)')
#
# cursor.execute('CREATE TABLE History (user Varchar(32), name Varchar(32), time_sell datetime)')
#
# cursor.executemany('INSERT INTO Products VALUES (?, ?, ?)', [('Cheese', 1, 500),
#                                                                                  ('Milk', 2, 70)])
# cursor.executemany('INSERT INTO History VALUES (?, ?, ?)', [('Max', 'Cheese', datetime.now()), ('Alex', 'Milk', datetime.now())])

cursor.execute('''SELECT * FROM History WHERE user == "Max"''')
print(cursor.fetchall())
conn.commit()