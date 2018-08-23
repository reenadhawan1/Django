from flask import Flask, render_template,request ,redirect,session,flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)

app.secret_key = 'DB'

mysql = connectToMySQL('emails')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validateEmail', methods=['POST'])
def validateEmial():
    session['email'] = request.form['email']
    email = mysql.query_db(f'select email from emails where email = "{session["email"]}"')
    print(session['email'].upper())
    if email:
        if not EMAIL_REGEX.match(session['email']):
            flash('Email format is not valid!')
            return redirect('/')
        elif session['email'].upper() in email[0]['email'].upper():
            flash(f'{session["email"]} already exists.')
            return redirect('/')
    else:
        query = 'insert into emails (email) values (%(email)s);'
        data = {'email': session['email']}
        mysql.query_db(query,data)

    return redirect('/success')

@app.route('/success')
def success():
    emails = mysql.query_db('select email,created_at from emails')
    return render_template('success.html', emails = emails)


app.run(debug=True)