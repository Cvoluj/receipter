import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from serializers.smtp import SMTP


class EmailService:
    @staticmethod
    def send_receipt(email: str, subject: str, body: str, smtp: SMTP):
        msg = MIMEMultipart()
        msg['From'] = smtp.smtp_email
        msg['To'] = email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'html'))

        try:
            with smtplib.SMTP_SSL(smtp.smtp_server, smtp.smtp_port) as server:
                server.login(smtp.smtp_email, smtp.smtp_password)
                server.send_message(msg)
        except Exception as e:
            print(f"Failed to send email: {e}")
            raise 
        print(body)
