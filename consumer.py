import pika
import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calcul_queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    message = json.loads(body)
    request_id = message["id"]
    operation = message["operation"]

    first_nb, operator, second_nb = operation.split()
    first_nb = float(first_nb)
    second_nb = float(second_nb)

    if operator == "+":
        result = first_nb + second_nb
    elif operator == "-":
        result = first_nb - second_nb
    elif operator == "*":
        result = first_nb * second_nb
    elif operator == "/":
        result = first_nb / second_nb

    r.set(str(request_id), result)

    print(f"Processing calculation with ID {request_id} and operation {operation}")

channel.basic_consume(queue='calcul_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
