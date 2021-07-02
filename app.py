from flask import Flask,render_template
from dao import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template("list.html",todos=get_todos())

@app.route('/about')
def about():
    return render_template("about.html",author=get_author())

@app.route('/todo_details')
def todo_details():
    return render_template("todo_details.html")

if __name__ == '__main__':
    app.run(debug=True,port=8000)
