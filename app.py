from flask import Flask
app = Flask(__name__)   #creates a flask object that will be run
@app.route('/login')         #main route
def root():
    return 'Hello'



#TO START SERVER ON LOCAL, USE python -m flask run