import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='calcul_queue')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    message = json.loads(body)
    request_id = message["id"]
    operation = message["operation"]
    
    print(f"Processing calculation with ID {request_id} and operation {operation}")

channel.basic_consume(queue='calcul_queue',
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
