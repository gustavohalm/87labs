Teste de Python
Nescesário ter instalado Python 3.x e pip

Para criação dos endpoints foi utilizado a bibliteca endpoints (https://github.com/Jaymon/endpoints) que utiliza o WSGI.


<code>
$ pip install endpoints
</code>


Faça o clone do projeto

<code>
$ git clone https://github.com/gustavohalm/87labs.git
</code>



Agora é só acessar o o diretório 

<code>
$ cd 87labs
</code>



E inicializar usando o WSGI Server

<code>
$ endpoints --prefix=controllers --host=localhost:8000
</code>


Realizar os testes, via Postman

Calculo do imposto

```
POST /tax

Payload

{
  "name": "Magic Mouse",
  "height": "0.75",
  "length": "1.10",
  "width": "0.60",
  "weight": "400",
  "price": "150.00"
}

Response

{
  "tax": "59.40"
}
```

Adicionar produtos

```
POST /

{
  "name": "Magic Mouse",
  "height": "0.75",
  "length": "1.10",
  "width": "0.60",
  "weight": "400",
  "price": "150.00"
}

Response
{
 "id": 1
}
```

Retornar todos os produtos

```

GET / 
Response
[
    
{
  "id": 1
  "name": "Magic Mouse",
  "height": "0.75",
  "length": "1.10",
  "width": "0.60",
  "weight": "400",
  "price": "150.00"  
},
  
{
  "id": 2
  "name": "Magic Mouse",
  "height": "0.75",
  "length": "1.10",
  "width": "0.60",
  "weight": "400",
  "price": "150.00",'
  
}

]

```

Retornar um produto especifico

```
GET /:id

GET /1

Response
  
{
  "id": 1
  "name": "Magic Mouse",
  "height": "0.75",
  "length": "1.10",
  "width": "0.60",
  "weight": "400",
  "price": "150.00" 
}

```
