import sqlite3

conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute("DELETE FROM todos")
#todos = c.fetchall()

# print(todos)

#for t in todos:
print("TODOS DELETED")


conn.commit()
conn.close()
 
#rowid, todo 