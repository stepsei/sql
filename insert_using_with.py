import sqlite3

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO population VALUES('New Town City',\
		'NT', 4500345)")
	c.execute("INSERT INTO population VALUES('San Accra',\
		'TE', 5679893)")
