from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'Main Page'

@app.route('/play')
def index():
    return render_template("index.html",num = int(3))

@app.route('/play/<x>')
def playX(x):
    return render_template("index.html", num = int(x))

@app.route('/play/<x>/<color>')
def playxc(x,color):
    return render_template("index.html", num = int(x), col = color)

app.run(debug=True)