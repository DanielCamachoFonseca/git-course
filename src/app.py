from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "¡Index!"

@app.route('/saludo')
def greating():
    return "¡Hola a todos!"


@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    sum_num = a + b
    return f"La suma es: {str(sum_num)}"

@app.route('/res/<int:a>/<int:b>')
def res(a: int, b: int):
    res_num = a - b
    return f"La resta es: {str(res_num)}"
