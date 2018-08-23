from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key = 'DB'

@app.route('/')
def index():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1                                                           
    print(session)
    print(request.cookies)
    return render_template('index.html', count = session['count'])

@app.route('/add')
def add():
    session['count'] += 1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.pop('count')
    return redirect('/')

app.run()