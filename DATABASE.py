import sqlite3

conn = sqlite3.connect('mytodos.db')
c = conn.cursor()

for i in range(5):
    todo = input("Enter season")
    episode = input("Enter episode")
    c.execute("INSERT INTO todos VALUES ('"+todo+" "+episode+"')")
print(todo,episode, "is inserted")
c.execute("SELECT *,rowid FROM todos")
todos = c.fetchall()

for t in todos:
    print(t)


conn.commit()
conn.close()


