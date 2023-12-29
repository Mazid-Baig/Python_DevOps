from flask import Flask

#Creating a Flask app instance
app = Flask(__name__)

#Decorator performs the action before the execution of the function.
@app.route('/')

def hello():
    return "hello, world"

app.run('0.0.0.0')

#flask runs on a default port 5000



