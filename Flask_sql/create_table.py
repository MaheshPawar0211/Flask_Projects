import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
#create_table= "DROP TABLE users"
#cursor.execute(create_table)
create_table= "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,username text,password text)"
cursor.execute(create_table)
create_table= "CREATE TABLE IF NOT EXISTS employee (name text,salary real)"
cursor.execute(create_table)
#cursor.execute("INSERT INTO employee VALUES ('test',1000)")
connection.commit()
connection.close()
