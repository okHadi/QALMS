from logindata import logging
from flask import Flask, render_template, request, redirect, url_for    #render_template() looks for a template (HTML file) in the templates folder.
app = Flask(__name__)   #creates a flask object that will be run



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if logging(request.form['username'], request.form['password']) == "Login failed":
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template("login.html", error=error)          #we can pass the values to be shown in the login.html as parameters of render_template


app.route('/')
def home():
    return render_template("home.html")












#TO START SERVER ON LOCAL, USE python -m flask run