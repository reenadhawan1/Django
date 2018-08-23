from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    print(request.form)
    return render_template('results.html', name = request.form['name'], location= request.form['location'], lang= request.form['language'], comment= request.form['comments'])



app.run(debug=True)