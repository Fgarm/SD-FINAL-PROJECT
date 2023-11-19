import json

from channels.generic.websocket import WebsocketConsumer

class DocumentConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        # self.user = self.scope["user"]

    def disconnect(self, close_code):
        # TODO: liberar locks nos docs? 
        pass

    def receive(self, text_data):
        # aqui a gente recebe as msgs
        # e tem que redirecionar pra os outros clientes no doc
        # as mudanças nele
        
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))