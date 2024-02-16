from flask import Flask, request, jsonify
import pika
import json
import uuid

app = Flask(__name__)
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
        "operation": f"{first_nb}{operation}{second_nb}"
    }
    channel.basic_publish(exchange='',
                          routing_key='calcul_queue',
                          body=json.dumps(message))
    
    return jsonify({"message": "Calculation request sent to RabbitMQ", "id": request_id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
