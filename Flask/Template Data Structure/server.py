from flask import Flask, render_template
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(debug=True)