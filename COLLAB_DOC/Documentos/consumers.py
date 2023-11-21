import json
import pika

from channels.generic.websocket import WebsocketConsumer

class DocumentConsumer(WebsocketConsumer):
    documento_id = "asdfg"
    connection = ""
    channel = ""
    def callback(ch, method, properties, body):
        # enviar esse dado pelo websocket pro cliente
        print("Recebeu do RabbitMQ")
        self.send(text_data=json.dumps({"message": body}))
        print("Enviou Websocket")
        # print(f" [x] {method.routing_key}:{body}")
        
    
    def connect(self):
        # self.user = self.scope["user"]
        print("Começou a conectar")
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        
        # declarada em outro lugar, mas vai que precisa aqui
        # channel.exchange_declare(exchange='documentos',
        #                 exchange_type='direct')
        
        #declara uma fila
        result = self.channel.queue_declare(queue='', exclusive=True)
        print("Declaro Fila")
        # binda essa fila pra ouvir coisas desse doc
        self.channel.queue_bind(exchange='documentos',
                       queue=result.method.queue,
                       routing_key=self.documento_id)
        
        print("Bindo Fila")
        self.channel.basic_consume(
        queue=result.method.queue, on_message_callback=self.callback, auto_ack=True)
        print("Detalhou fila")
        
        self.accept() # deixar por ultimo, e aceitar só se o user for valido pro doc
        print("Iniciou a conexão websocket")
        # TODO: pegar e enviar o estado atual do documento
        
        self.channel.start_consuming()
        # https://stackoverflow.com/questions/56165657/unable-to-stop-consuming-in-pika
        # colocar o canal pra ouvir por sla, 0.1 segundo a cada 3 segundos, é sincronia o suficiente
        print("Conexão deu certo / ouvindo fila")
        # BUG: se alguém fizer uma mudança dps de pegar o doc, antes de consumir, 
        # tem q lidar com perder um pacote
        # creio q vou sempre reenviar o pedaço, ent sla
        

    def disconnect(self, close_code):
        print("Desconectou")
        # TODO: liberar locks nos docs?
        # fechar a queue (aparentemente não precisa)
        pass

    def receive(self, text_data):
        # aqui a gente recebe as as mudanças que o cliente fez nos docs
        print("Começou a receber websocket")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        # e tem que redirecionar pra os outros clientes no doc elas
        channel.basic_publish(exchange='documentos',
                      routing_key=self.documento_id,
                      body=message)
        print("Publicou no RabbitMQ")

        # aqui a gente envia de volta pro nosso cliente
        # da pra enviar alguma outra coisa. (talvez os pedaços que mudaram)
        # n precisa pq o próprio nosso RabbitMQ envia
        # self.send(text_data=json.dumps({"message": message})) 
        # print("Publicou no websocket")