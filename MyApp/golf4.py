import flask
app = flask.Flask("golf4")
from statistics import mean

def get_html(page_name):
    html_file = open (page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_scores():
    golfdb = open ("scores.txt")
    content = golfdb.read()
    golfdb.close
    scores = content.split("\n") #collection of splitted scores
    scores.pop() #remove the last item of the list which is an empty line
    return scores

def add_score(a):
    golfdb = open ("scores.txt","a")
    golfdb.write(a + "\n") 
    golfdb.close()
    
    
#This is the route to the homepage named "golf"
@app.route("/")
def homepage():
    return get_html("golf") 

#This is the route to the dynamic scores page named "scores"
@app.route("/scores")
def scores():
    html_page = get_html("scores")
    scores = get_scores()#a collection that contains all the scores
    actual_values = "" #empty string

    for score in scores:
        actual_values += "<p>" + score + "</p>"
    return html_page.replace("SCORES", actual_values)

#this is the route to the "add score" page
@app.route("/add")
def add():
    html_page = get_html("scores")
    query = flask.request.args.get("n")
    add_score(query)
    result = "your score was succesfully added" #string
    return html_page.replace("SCORES", result)

@app.route("/calculate")
def calculate():
    html_page = get_html("scores")
    scores = get_scores()#a collection of strings that contains all the scores
    index = "" #empty string
    par = 72 #this is the theorical score anyone should do, in fact everbody except some professional are doing higher scores.
 
    index = "Your updated golf index is now: " + str(mean((int(score)-int(par)) for score in scores))
    return html_page.replace("SCORES", index)
    

#cd MyApp : to access the folder
#cd .. : to go back
#this is the command to run flask
#$env:FLASK_APP="golf4.py" 
#flask run