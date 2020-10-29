import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
create_querry = "CREATE TABLE Users (id int, username text, password text)"
users = [(1, 'Aman', '123'), 
    (2, 'aman', '1234')
]
insert_querry  = "insert into Users values(?, ?, ?)"
select_querry = "Select * from Users"
# cursor.execute(create_querry)
# cursor.executemany(insert_querry, users)
for i in cursor.execute(select_querry):
    print(i)
connection.commit()
connection.close()