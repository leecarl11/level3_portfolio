from flask import Flask, render_template
from view import my_view
#creating an instance of a Flask class called app
app = Flask(__name__)
app.register_blueprint(my_view)
@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404
#using the route() method on our app. this builds endpoints - i.e it tells our app how to run depending on the browser. for example, if my user visits www.domain.com/ - the index() function will then run, the job of the index function is to return hello world
#this if statement is the last thing on our app - it allows the initialisation of the app. Debugis set to true, and we pick a port to run on. 5000 is default and 8000 is linked to the debugger
if __name__=="__main__":
    app.run(debug=True, port=8000)
    
#we have just been setting up different functions to return bits of informations for us based on what we type in the browser. flask apps need a very specific file structure to work from,this is how they must have been written to work, if we want to actually make WEBPAGES rather than just return random strings, if we want a page to come back us it must be in a specific file structure(create a templates folders in the flask-project folder and also create a static folder inside the flask-project folder also)if we are wanting our flask to manage WEBPAGES which we are in this case we are making a web application we must have this file structure, WEBPAGES and html files will go in templates folder , static files like images css, javascript will all go in the static folder, we must have this structure for flask app to work properly