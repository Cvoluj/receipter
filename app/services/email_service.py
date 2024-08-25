import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import server_settings

class EmailService:
    @staticmethod
    def send_receipt(to_email: str, subject: str, body: str):
        # msg = MIMEMultipart()
        # msg['From'] = server_settings.from_email
        # msg['To'] = to_email
        # msg['Subject'] = subject

        # msg.attach(MIMEText(body, 'plain'))

        # try:
        #     with smtplib.SMTP(server_settings.smtp_server, server_settings.smtp_port) as server:
        #         server.starttls()
        #         server.login(server_settings.smtp_user, server_settings.smtp_password)
        #         server.send_message(msg)
        # except Exception as e:
        #     print(f"Failed to send email: {e}")
        #     raise 
        print(body)
