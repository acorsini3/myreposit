import flask
app = flask.Flask("render")
from flask import render_template


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


    
#this is the command to run flask
#$env:FLASK_APP="render.py" 
#flask run