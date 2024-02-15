from flask import Flask, request, jsonify
import csv
import redis
import uuid
from datetime import datetime, timedelta
import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



@app.route('/operation', methods=['POST'])
def operation():
    data = request.get_json()
    
    first_nb = float(data[0])
    operation = data[1]
    second_nb = float(data[2])

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
    
    return jsonify({random_uuid}), 201



# Nouvelle route pour la racine ("/")
@app.route('/')
def home():
    return "Bienvenue !"

@app.route('/operation', methods=['GET'])
def get_result_from_id():
    id = request.args.get('id')
    operation_result = r.get(id)
    if operation_result:
        return operation_result
    else:
        return "Event not found", 404
    

