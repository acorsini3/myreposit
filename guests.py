import flask
app = flask.Flask("guests")

def get_html(page_name):
    html_file = open (page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

def get_guests():
    guestsdb = open ("guests.txt")
    content = guestsdb.read()
    guestsdb.close
    guests = content.split("\n") #collection of splitted names
    return guests

@app.route("/")
def homepage():
    return get_html("IndexGuests") 
    


@app.route("/guests")
def guests():
    html_page = get_html("guests")
    guests = get_guests()
    actual_values = "" #empty string


    for guest in guests:
        actual_values += "<p>" + guest + "</p>"

    return html_page.replace("GUESTS", actual_values)

    #this is the command to run flask
    #$env:FLASK_APP="guests.py" 
    #flask run
