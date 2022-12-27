from logindata import logging
from scraping import login_and_scrape
from flask import Flask, render_template, request, redirect, url_for, session    #render_template() looks for a template (HTML file) in the templates folder.
app = Flask(__name__)   #creates a flask object that will be run
app.secret_key = 'eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJJc3N1ZXIiOiJJc3N1ZXIiLCJVc2VybmFtZSI6IkphdmFJblVzZSIsImV4cCI6MTY3MjE2MTYwMSwiaWF0IjoxNjcyMTYxNjAxfQ.uqmoow_iw48tGBIsBlcc_rWcqEVST_-k9r1yolp21Yw' #creates a secret key for the session



@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        session['password'] = password
        if logging(username, password) == "Login failed":
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))     #sends the login data to the home page, so we can properly login again
    return render_template("login.html", error=error)          #we can pass the values to be shown in the login.html as parameters of render_template


@app.route('/', methods=['GET'])
def home():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    else:
        username = session.get('username', '')
        password = session.get('password', '')
        login_and_scrape(username, password)
        return render_template("home.html")












#TO START SERVER ON LOCAL, USE python -m flask run