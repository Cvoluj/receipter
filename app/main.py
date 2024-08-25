import logging

from config import server_settings
from services.template_service import TemplateService
from services.email_service import EmailService
from receipt_consumer import ReceiptConsumer


logging.basicConfig(level=server_settings.LOG_LEVEL)

if __name__ == "__main__":
    consumer = ReceiptConsumer(TemplateService(), EmailService())
    consumer.consume()