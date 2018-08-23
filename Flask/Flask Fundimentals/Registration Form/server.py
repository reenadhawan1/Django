from flask import Flask, render_template, redirect,session,request,flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'DB'

@app.route('/')
def index():
    return render_template('index.html'
    ,first_name = session.get('first name','')
    ,last_name = session.get('last name','')
    ,email = session.get('email',''))

@app.route('/register', methods=['POST'])
def register():
    session['first name'] = request.form['first_name']
    session['last name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm password'] = request.form['confirmPassword']
    errors = False
    for key,val in list(session.items()):
        if len(val) < 1:
            flash(f'{key} cannot be blank!')
            errors = True
    if not session['first name'].isalpha() or not session['last name'].isalpha():
        flash('Names cannot have numbers!')
        errors = True
    elif not EMAIL_REGEX.match(session['email']):
        flash('Email format is not valid')
        errors = True
    elif len(session['password']) < 8:
        flash('Passwords must be at least 8 charachters long')
        errors = True
    elif session['password'] != session['confirm password']:
        flash('Your passwords do not match')
        errors = True
    if errors:
        return redirect('/')
    return redirect('/registered')

@app.route('/registered')
def registered():
    return render_template('registered.html')

app.run(debug=True)