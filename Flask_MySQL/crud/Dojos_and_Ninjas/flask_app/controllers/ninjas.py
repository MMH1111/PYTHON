from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

# OUTLINE
# "index.html"
# "show_dojo.html"
# "create_ninja.html"

# DISPLAY ROUTES --------------------------------
@app.route("/ninjas")
def new_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("create_ninja.html", all_dojos = dojos)


# ACTION ROUTES -----------------------------
@app.route("/ninjas/create", methods = ["POST"])
def create_ninja():
    Ninja.create(request.form)
    dojos_id = request.form["dojos_id"]
    return redirect(f"/dojos/{dojos_id}")