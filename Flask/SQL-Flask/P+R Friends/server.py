from flask import Flask, render_template, redirect,request
from mysqlconnection import connectToMySQL
app = Flask(__name__)

mysql = connectToMySQL('friendsdb')

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print(mysql.query_db("SELECT * FROM friends"))
    return render_template('index.html', friends=all_friends)

@app.route('/add', methods=['POST'])
def add():
    mysql.query_db(f"insert into friends (first_name, last_name,occupation)values('{request.form['first_name']}','{request.form['last_name']}','{request.form['occupation']}')")
    return redirect('/')

app.run(debug=True)