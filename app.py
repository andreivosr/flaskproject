from flask import Flask, jsonify, request
app = Flask(__name__)

objetos = []

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

@app.route('/objetos', methods=["GET"])
def listar_objetos():
    return jsonify(objetos)

if __name__ == "__main__":
    app.run(debug=True)