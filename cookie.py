import flask

app = flask.Flask("cookie")

from flask import request, make_response
from flask.templating import render_template

#This is the homepage

@app.route("/")
def homepage():
    return render_template('cookie.html')

@app.route('/setcookie',methods = ['POST', 'GET'])
def setcookie():
        if request.method == 'POST':
            user = request.form['username']

        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)

        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return 'weclome' + name


#this is the command to run flask
 #$env:FLASK_APP="cookie.py" 
 #flask run

