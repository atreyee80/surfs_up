
#9.5.1 Set up the flask and create a route
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world lopa'


