from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola Mundo!"


@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    sum_num = a + b
    return f"La suma es: {str(sum_num)}"