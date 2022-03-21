from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from flask_app import app
from flask_app.models.dojo import Dojo

# OUTLINE
# "index.html"
# //Display Routes

# "show_dojo.html"
# "create_ninja.html"

# DISPLAY ROUTES -----------------------

# This one works fine
@app.route("/")
def index():
    dojos = Dojo.get_all_dojos()
    return render_template("index.html", all_dojos = dojos)
# END This one works fine

@app.route("/dojos/<int:id>")
def show_dojo(id):
    # print("I AM INSIDE OF SHOW_DOJO")
    data = { "id": id }
    # print("I tried to store into data")
    # print(data)
    dojo = Dojo.get_one_with_ninjas(data)
    
    return render_template("show_dojo.html", dojo = dojo)

@app.route("/dojos/create")
def new_dojo():
    return render_template("add_dojo.html")


# ACTION ROUTES -----------------------

@app.route("/dojos/create", methods = ["POST"])
def create_dojo():
    Dojo.create_dojo(request.form)
    return redirect('/')


