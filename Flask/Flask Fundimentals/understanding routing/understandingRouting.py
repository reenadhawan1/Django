from flask import Flask  
app = Flask(__name__)    

@app.route('/')
def hello():
    return "Hello World"

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return "Hi "+name

@app.route('/repeat/<num>/<stuff>')
def repeat(num,stuff):
    return (f'{stuff} \n') * int(num)
    

if __name__=="__main__": 
    app.run(debug=True)  