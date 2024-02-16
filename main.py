from flask import Flask, request, jsonify
import redis
import uuid
import json

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/operation', methods=['POST'])
def operation():
    data = request.get_json()
    
    first_nb = float(data.get("0"))
    operation = data.get("1")
    second_nb = float(data.get("2"))

    if operation == "+":
        result = first_nb + second_nb
    elif operation == "-":
        result = first_nb - second_nb
    elif operation == "*":
        result = first_nb * second_nb
    elif operation == "/":
        result = first_nb / second_nb
    
    random_uuid = uuid.uuid4()
    r.set(str(random_uuid), result)
    
    return jsonify({"id": str(random_uuid)}), 201  # Convert UUID to string before returning in JSON

@app.route('/')
def home():
    return "Bienvenue !"

@app.route('/operation', methods=['GET'])
def get_result_from_id():
    id = request.args.get('id')
    operation_result = r.get(id)
    if operation_result:
        return jsonify({"result": float(operation_result)})  # Ensure result is converted to float before returning
    else:
        return "Event not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
