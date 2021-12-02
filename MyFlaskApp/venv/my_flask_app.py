#Import dependicies
from flask import Flask

#Set up the Database

#Set Up Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return 'Hi world'