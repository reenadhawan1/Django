from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    num = 8
    return render_template('index.html', x=int(num), r ='box1', b = 'box2')

@app.route('/<y>')
def index1(y):
    return render_template('index.html', x=int(y), r ='box1', b = 'box2')

app.run(debug=True)