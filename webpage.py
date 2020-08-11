from flask import Flask
from flask_cors import CORS
app=Flask(_name_)
CORS(app)
@app.route("/")
def hello():
    img="https://www.gstatic.com/webp/gallery3/1.sm.png"
      return img
app.run(port="1308")