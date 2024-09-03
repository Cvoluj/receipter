from dataclasses import dataclass
from cryptography.fernet import Fernet


from config import server_settings


@dataclass
class SMTP:
    name: str
    smtp_server: str
    smtp_port: int
    smtp_email: str
    smtp_password: str

def decrypt_smtp_password(encrypted_password: str) -> str:
    fernet = Fernet(server_settings.ENCRYPTION_KEY)
    return fernet.decrypt(encrypted_password.encode()).decode()


def serialize_to_smpt_dataclass(data: dict) -> SMTP:
    return SMTP(name=data['name'],
        smtp_server=data['smtp_server'],
        smtp_port=data['smtp_port'],
        smtp_email=data['smtp_email'],
        smtp_password=decrypt_smtp_password(data['smtp_password']),
    )
