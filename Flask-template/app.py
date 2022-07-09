from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>Hello  World!</h1>"

@app.route("/Debbie")
def Debbie():
    return "<h1>This is Debbie\'s</h1>"

if __name__=="__main__":
    app.run(debug=True, port=8000)
    
