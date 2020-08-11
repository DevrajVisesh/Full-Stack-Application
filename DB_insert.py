  
import sqlite3
todo = input("Enter todo: ")
episode = input("Enter Episode no.")
conn = sqlite3.connect('mytodos.db')
c = conn.cursor()
c.execute("INSERT INTO todos VALUES ('"+todo+" "+episode+"')")
print(todo, "is inserted")
print(episode, "is inserted")
conn.commit()
conn.close() 