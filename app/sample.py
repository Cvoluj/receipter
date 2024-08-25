import pika
import json

def send_test_message():
    # Connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    # Declare the queue
    channel.queue_declare(queue='receipt_queue')

    # Test message data
    message = {
        'email': 'customer@example.com',
        'subject': 'Your Receipt',
        'context': {
            'name': 'John Doe',
            'items': [
                {'name': 'Item 1', 'quantity': 2, 'price': 10.99},
                {'name': 'Proselyte of the Sakura Clan', 'quantity': 3,'price': 10.49},
            ],
            
        }
    }
    message['context']['total'] = 0
    for item in message['context']['items']:
        message['context']['total'] += item['quantity'] * item['price']
    # Convert the message to a JSON string
    message_body = json.dumps(message)

    # Publish the message to the queue
    channel.basic_publish(exchange='',
                          routing_key='receipt_queue',
                          body=message_body)

    print(" [x] Sent 'Receipt email message'")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    send_test_message()
