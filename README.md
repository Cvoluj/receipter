# receipter

This is a MVP microservice for sending html formatted email. 

## Features

- Python 3.12+
- RabbitMQ for microservices communication [pika](https://github.com/pika/pika/)
- Configuration via `.env` file
- single file for each class
- Docker-ready (see [here](#docker))

## Installation

### Python Quickstart Guide
To run this microservice you need to follow this guide:

* Temporary only no docker route

1. Clone the repository. `git clone https://github.com/Cvoluj/receipter.git .`
2. `cp .env.example .env`
3. Run `python .\app\generate_fernet_key.py`
4. Paste generated code to `ENCRYPTION_KEY=` in .env
4. Run RabbitMQ `docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management`
5. No docker:
   1. Have the following prerequisites: python 3.12+, libraries
   2. `pip install -r reqiurements.txt`
   3. `python .\app\main.py`

6. On other service you must send to `RABBITMQ_QUEUE` JSON simmilar to this
```
{
  "email": "mail@example.com",
  "subject": "subject of mail",
  "context": {
    "name": "Service name",
    "items": [
      {
        "name": "Item name",
        "quantity": 3,
        "price": "4.50",
        "subtotal": "13.50"
      }
    ],
    "total": "13.50"
  },
  "smtp": {
    "name": "Service name",
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 465,
    "smtp_email": "smtp.service@example.com",
    "smtp_password": "<encrypted password>"
  }
}
```
