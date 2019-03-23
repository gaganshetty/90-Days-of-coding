import sqlite3

con = sqlite3.connect("groceries_sql.db")
cur = con.cursor()

cur.execute('''CREATE TABLE groceries(id INTEGER, name TEXT, quantity INTEGER )''')
cur.execute('''INSERT INTO groceries VALUES(1,'Bananas',4)''')
cur.execute('''INSERT INTO groceries VALUES(2,'Biscuits',2)''')
cur.execute('''INSERT INTO groceries VALUES(3, 'Berries',3)''')

cur.execute('''SELECT * FROM groceries''')
con.commit();