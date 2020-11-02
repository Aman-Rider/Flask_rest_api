import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items(name text, price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES('test', 1000.2)")
# result = cursor.execute("SELECT * FROM items")
# row = result.fetchall()
# for i in row:
#     print(i)
connection.commit()
connection.close()