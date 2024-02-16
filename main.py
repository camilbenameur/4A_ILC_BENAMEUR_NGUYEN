from flask import Flask, request, jsonify
import pika
import json
import uuid
import redis


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calcul_queue')

@app.route('/operation', methods=['POST'])
def operation():
    data = request.get_json()
    
    first_nb = float(data.get("0"))
    operation = data.get("1")
    second_nb = float(data.get("2"))
    
    # Generate a UUID for the calculation request
    request_id = str(uuid.uuid4())
    
    # Send the calculation request along with the UUID to RabbitMQ
    message = {
    "id": request_id,
    "operation": f"{first_nb} {operation} {second_nb}"  # Add spaces between operands and operator
}

    
    channel.basic_publish(exchange='',
                          routing_key='calcul_queue',
                          body=json.dumps(message))
    
    return jsonify({"message": "Calculation request sent to RabbitMQ", "id": request_id}), 201

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
