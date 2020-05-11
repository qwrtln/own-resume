import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

create_table_work = "CREATE TABLE IF NOT EXISTS work (company STRING PRIMARY KEY, position STRING, summary TEXT)"
cursor.execute(create_table_work)

connection.commit()
connection.close()
