#Import Flask
from flask import Flask

#Create a new Flask App Instance
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
export FLASK_APP=app.py
flask run 

