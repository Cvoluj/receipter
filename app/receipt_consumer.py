import pika
import json


from services.email_service import EmailService
from services.template_service import TemplateService
from serializers.smtp import serialize_to_smpt_dataclass
from config import server_settings

class ReceiptConsumer:
    def __init__(self, template_service: TemplateService, email_service: EmailService):
        self.template_service = template_service
        self.email_service = email_service

    def consume(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=server_settings.RABBITMQ_HOST))
        channel = connection.channel()

        channel.queue_declare(queue=server_settings.RABBITMQ_QUEUE)

        def callback(ch, method, properties, body):
            data = json.loads(body)

            email = data['email']
            subject = data['subject']
            context = data['context']
            smtp = serialize_to_smpt_dataclass(data['smtp'])
            body = self.template_service.render_receipt(context)
            self.email_service.send_receipt(email, subject, body, smtp)

        channel.basic_consume(queue=server_settings.RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)

        print('Waiting for messages...')
        channel.start_consuming()
