import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Documento
from .serializers import DocumentoSerializer

class DocumentConsumer(WebsocketConsumer):
    client_id = ""
    def connect(self):
        self.documento_id = self.scope["url_route"]["kwargs"]["documento_id"]
        self.documento_group_id = f"doc_{self.documento_id}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.documento_group_id, self.channel_name
        )

        self.accept()
        version = 1
        newEndPos = 0
        data = ""
        try:
            doc = Documento.objects.get(id=self.documento_id)
            version = doc.versao
            data = doc.conteudo
            newEndPos = len(doc.conteudo)
        # verificando se o user selecionado existe
        except Documento.DoesNotExist:
            dict = {}
            dict["id"] = self.documento_id
            dict["versao"] = version
            dict["conteudo"] = ""
            serializer = DocumentoSerializer(data=dict)
            if serializer.is_valid():
                serializer.save()
            # Enviando o documento no estado inicial
        self.send(text_data=json.dumps(
                    {
                    'version' : version,
                    'type' : 'doc.start',
                    'data': data
                    }))
        
        


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.documento_group_id, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json["type"] == "user.signin":
            if self.client_id == "":
                self.client_id = text_data_json["client_id"]
                # print(self.client_id)
            
        if text_data_json["type"] == "doc.change":
            doc = Documento.objects.get(id=self.documento_id)
            #print(text_data_json)
            # Enviar as mudanças para serem salvas no db
            if text_data_json["version"] == doc.versao + 1:
                doc.versao += 1
                documento = doc.conteudo
                # console.log(typeof(documento))
                start_index = text_data_json['newStartPos']
                if text_data_json['startPos'] < start_index:
                    start_index = text_data_json['startPos']
                start_subsection = documento[:start_index]
                #print(start_subsection)
                end_subsection = documento[text_data_json['endPos']:]
                #print(end_subsection)
                meio = ""
                if text_data_json['data'] == "backspace" or text_data_json['data'] == "delete":
                    pass
                else:
                    meio = text_data_json['data']
                
                doc.conteudo = start_subsection + meio + end_subsection
                doc.save()
                # Send message to room group
                async_to_sync(self.channel_layer.group_send)(
                    self.documento_group_id, text_data_json
                )
            

            
            

    # Receive message from room group
    def doc_change(self, event):
        # message = event["message"]

        # Send message to WebSocket
        # print(event)
        self.send(text_data=json.dumps(event))