from flask import Flask, request, jsonify

# Variables de instanciado
app = Flask(__name__)


# Funciones
@app.route('/myroute', methods=['GET'])
def hello_world():
    # You can convert that variable into a json string like this
    json_text = jsonify(some_data)

    # And then you can return it to the front end in the response body like this
    return json_text

@app.route('/todos', methods=['GET'])
def handle_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return todos

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return todos


# Codigo / variables
todos = [{ "label": "My first task", "done": False }]
some_data = { "name": "Bobby", "lastname": "Rixer" }


# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)