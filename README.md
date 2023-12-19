# Collabing Docs
## Descrição da aplicação
Uma Aplicação de edição de documentos de forma colaborativa.
### funcionalidades
Criação e edição de documentos. Compartilhamento para outros usuários editarem o mesmo documento.
## Fluxo

### Fluxo Princial
#### Usuário
- O usuário se cadastrará ou logará no sistema (REST)
- O usuário começará a editar um documento (REST)
- O usuário irá editar o documento (mudanças enviadas via webSocket)
- Caso outro usuário edite o documento, mudanças apareçerão para esse usuário (mudanças recebidas via webSocket)

### REST Endpoints
#### - `/login` 
#### - `/cadastro`
#### - `/home`
#### - `/edit`
### Comunicação webSocket
#### - Envio de alterações no documento
```py
{
    "chunk_id" : int,
    "version"  : int,
    "data"     : str
}
```
#### - Recebimento de alterações no documento
```py
{
    "chunk_id" : int,
    "version"  : int,
    "data"     : str
}
```


### Características de Sistemas Distribuidos
Concorrência e paralelismo são desafios enfoque nessa aplicação
## Arquitetura
![Diagrama da arquitetura](https://github.com/Fgarm/SD-FINAL-PROJECT/blob/main/DOCUMENTATION/Arquitetura.png)
## Tecnologias

API REST para conexão e gerenciamento de documentos, e comunicação por webSockets para edição de documentos de forma concorrente
## Equipe
Guilherme Augusto Rodrigues Maturana
