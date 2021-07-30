import flask
app = flask.Flask("escape")
from markupsafe import escape


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


    
#this is the command to run flask
#$env:FLASK_APP="escape.py" 
#flask run

#http://127.0.0.1:5000/Alex