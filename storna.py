from flask import Flask, render_template
from lista import generator
from name import imie
app = Flask(__name__)


lista = generator()
your_name = imie()

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/test/")
def template_test():
    return render_template('template.html', my_string=your_name, my_list=lista)

@app.route('/app/')
def hi():
    return "Hello there"


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
