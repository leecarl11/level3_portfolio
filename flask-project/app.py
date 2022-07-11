from flask import Flask
#creating an instance of a Flask class called app
app = Flask(__name__)

#using the route() method on our app. this builds endpoints - i.e it tells our app how to run depending on the browser. for example, if my user visits www.domain.com/ - the index() function will then run
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

#this if statement is the last thing on our app - it allows the initialisation of the app. Debugis set to true, and we pick a port to run on. 5000 is default and 8000 is linked to the debugger
@app.route("/Debbie")
def Debbie():
    return "Debbie\'s page"

if __name__=="__main__":
    app.run(debug=True, port=8000)