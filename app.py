from flask import Flask,render_template,request,redirect
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
    id=request.args.get('id')
    print(f'id={id}')
    return render_template("todo_details.html",todo=get_todo(id))

@app.route('/add_todo')
def add_todo():
    return render_template("add_todo.html")

@app.route('/add_todo',methods=['POST'])
def add_todo_post():
    nazwa=request.form['nazwa']
    opis=request.form['opis']
    priorytet=request.form['priorytet']
    t=ToDo(None,nazwa,opis,priorytet)
    print(nazwa,opis,priorytet)
    return redirect('/list')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
