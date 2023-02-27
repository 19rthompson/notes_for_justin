import sqlite3

connection = sqlite3.connect("movies_db.db")
cursor = connection.cursor()

#note the lack of semi colon at the end of the string
#you only nees semi colons if your'e in the command line
cursor.execute("INSERT INTO movies (name,rating,genre) VALUES ('Avatar: The Last Airbender',1,'Super bad')")
connection.commit()

cursor.execute("SELECT * FROM movies")

records = cursor.fetchall()

print(records)