import sqlite3

connection = sqlite3.connect("test_data.db")
cursor = connection.cursor()

create_table_work = "CREATE TABLE IF NOT EXISTS work (company STRING PRIMARY KEY, position STRING, summary TEXT)"
cursor.execute(create_table_work)

create_table_basics = "CREATE TABLE IF NOT EXISTS basics (name STRING PRIMARY KEY, summary TEXT, email STRING)"
cursor.execute(create_table_basics)

connection.commit()
connection.close()
