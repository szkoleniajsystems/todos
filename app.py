from flask import Flask,render_template
from dao import get_author

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template("list.html")

@app.route('/about')
def about():
    return render_template("about.html",author=get_author())

if __name__ == '__main__':
    app.run(debug=True,port=8000)
