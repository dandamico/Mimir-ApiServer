import pika
import uuid
import notebook
from models import Notebook
import json
import os

class Rabbit:
    host= os.environ.get("HOST_RABBITMQ")
    user= os.environ.get("USER_RABBITMQ")
    password= os.environ.get("PASSWORD_RABBITMQ")

class RpcClient(Rabbit):

    def __init__(self):
        credentials = pika.PlainCredentials(self.user, self.password)
        params = pika.ConnectionParameters(self.host, 5672, '/', credentials)
        self.connection = pika.BlockingConnection(params)

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, message):

        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(message)) 