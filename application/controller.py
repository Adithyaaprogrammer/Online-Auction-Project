from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.database import db
from application.models import *
from sqlalchemy import func
import matplotlib.pyplot as plt 

@app.route("/")
def intro():
    return render_template("intro_page.html")    
@app.route("/user", methods=["GET", "POST"])
def user():
    if request.methods =="POST":
        username = request.form["username"]
        password = request.form["password"]

    else:    
        return render_template("user.html")
@app.route("/admin", methods=["GET", "POST"]) 
def admin():
    if request.methods =="POST":
        username = request.form["username"]
        password = request.form["password"]
    else:
        return render_template("admin.html")



