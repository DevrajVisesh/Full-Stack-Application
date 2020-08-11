from flask import Flask
import sqlite3
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route('/<name>')
def hello(name):
    return "Hello World!"+name

@app.route('/Create_db/<database>')
def create(database):
    conn = sqlite3.connect(database+'.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE todos
                 (todo text)''')
    conn.commit()
    conn.close()
    return database+" "+"Database is created"

@app.route('/db_insert/<todo>')
def insert(todo):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos VALUES ('"+todo+"')")
    #print(todo, "is inserted")
    #print(episode, "is inserted")
    conn.commit()
    conn.close()
    return "TODO ADDED"
    
@app.route('/get_todos')
def todos():    
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("SELECT rowid, todo From todos")
    todos = c.fetchall()
    todo_array = []
    for t in todos:
        todo_array.append(t)

    # print(todos)
    #for t in todos:
    #    print(t)
    conn.commit()
    conn.close()
    return json.dumps(todo_array)

@app.route('/deletetodos/<data>')
def delete(data):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos where rowid ='"+data+"'")
    conn.commit()
    conn.close()
    return "TODO DELETED"

@app.route('/updatetodos/<newvalue>/<rowid>')
def update(newvalue,rowid):
    conn = sqlite3.connect('mytodos.db')
    c = conn.cursor()
    c.execute("UPDATE todos SET todo ='"+newvalue+"' where rowid = '"+rowid+"'")
    conn.commit()
    conn.close()
    return "TODO UPDATED"
app.run(port="1308")

