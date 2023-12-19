# Collabing Docs
## Descrição da aplicação
Uma Aplicação de edição de documentos de forma colaborativa.
### Funcionalidades
Criação e edição de documentos. 
Compartilhamento para outros usuários editarem os mesmos documentos.
## Fluxo

### Fluxo Princial
#### Usuário
- O usuário entrará no sistema e escolherá um documento (REST)
- O usuário será direcionado a edição de um documento (REST)
- O usuário irá editar o documento (mudanças enviadas via webSocket)
- Um servidor será responsável por armazenar com autoridade a versão final do documento (receberá as mudanças e as compartilhará via webSocket)
- Caso outro usuário edite o documento, mudanças apareçerão para esse usuário (mudanças recebidas via webSocket)

### REST Endpoints
#### - `/home`
#### - `/edit`
### Comunicação webSocket
#### - Envio de identificação de um cliente ao servidor
```py
{
    'client_id' : str,
    'type' : 'user.signin'
}
```
#### - Primeiro envio do documento a um cliente
```py
{
    'version' : int,
    'type' : 'doc.start',
    'data': str
}
```
#### - Envio de alterações no documento
```py
{
    'version': int,
    'startPos': int,
    'endPos': int,
    'newStartPos': int,
    'type' : 'doc.change',
    'client_id': str,
    'data':  str
}
```
#### - Envio de identificação inicial ao servidor
```py
{
    'client_id': str,
    'type' : "user.signin"
}
```


### Características de Sistemas Distribuidos
Concorrência e paralelismo são desafios enfoque nessa aplicação
## Arquitetura
![Diagrama da arquitetura](https://github.com/Fgarm/SD-FINAL-PROJECT/blob/main/DOCUMENTATION/Arquitetura.png)
## Tecnologias

API REST para conexão e gerenciamento de documentos, e comunicação por webSockets para edição de documentos de forma concorrente

Gerenciamento das diferentes tecnologias utilizando python com Framework Django e Channels, com Banco de dados principal MySQL e banco secundário para funcionamento Pub/Sub Redis. Frontend composto por HTML, CSS e Javascript puro
## Equipe
Guilherme Augusto Rodrigues Maturana

## Como Rodar

1. Configure um arquivo local_settings.py, sobreescrevendo a variável ``DATABASES`` do settings.py com a sua database, e a variável ``CHANNEL_LAYERS`` com seu banco Redis

2. (Opcionalmente, crie um ambiente virtual, e) instale as dependencias de python com `python3 pip install -r requirements.txt`

3. Utilize o arquivo makefile para fazer e aplicar as migrações no seu banco de dados, com `make makemigrations` e `make migrate`.

4. Utilize `make runserver`, e acesse o website disponível em ```localhost:8000/home```
