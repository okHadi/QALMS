from flask import Flask, render_template
app = Flask(__name__)   #creates a flask object that will be run



@app.route('/login')         #main route
def root():
    return render_template("login.html")          #we can pass the values to be shown in the login.html as parameters of render_template















#TO START SERVER ON LOCAL, USE python -m flask run