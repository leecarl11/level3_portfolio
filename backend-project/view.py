from flask import Flask, Blueprint, render_template, url_for, redirect

my_view = Blueprint("my_view", __name__)
@my_view.route("/")
def index():
    return render_template("index.html")

@my_view.route("/Debbie")
def Debbie():
    return render_template("Debbie\'s.html")

@my_view.route("/Dhriti")
def Dhriti():
    return"<h1>This is Dhriti\'s App</h1>"
@my_view.route("/admin")
def admin():
    return render_template("admin.html")

@my_view.route("/page1")
def page1():
    return render_template("page1.html")
@my_view.route("/page2")
def page2():
    return render_template("page2.html")
@my_view.route("/page3")
def page3():
    return render_template("page3.html")
@my_view.route("/page4")
def page4():
    return render_template("page4.html")
@my_view.route("/page5")
def page5():
    return render_template("page5.html")

@my_view.route("/home")
@my_view.route("/js")
@my_view.route("/javascript")
def redirection():
    return redirect(url_for("my_view.index"))