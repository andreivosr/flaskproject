from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/eventos')
def eventos():
    return "Eventos"

@app.route('/ola/<nome>')
def ola(nome):
    return f"ola, {nome}"

@app.route('/produtos')
def produtos():
    produtos = ['aaa', 'bbb', 'ccc', 'ddd']
    return jsonify(produtos)