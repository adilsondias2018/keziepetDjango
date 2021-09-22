# Primeiros passos
Para instalar e rodar o Kenzie Pet é necessário primeiro fazer o clono do repositório no GitLab no seguinte endereço.

<https://gitlab.com/adilsondias/kenziepet>

# Este passo é para baixar o projeto
```Python
git clone  https://gitlab.com/<your_user>/kenzie_pet.git

# Criar um ambiente virtual
python3 -m venv venv

# Entrar no ambiente virtual
source venv/bin/activate

```
# Agora instala-se as depedências
Para isso basta digiar o seguinte comando

```Python
pip install -r requirements.txt

```
# Criando os bancos e as tabelas

```Python
./manage makemigrate

```
# Rodando a aplicação

```Python
./manage runserver

```

# Utlização
Para ultizar e entender melhor a API é recomendado o uso do Insomia ou outro aplicativo que faça a leitura de rotas

# Rotas da API:

## POST 

```Python
 post localhost:8000/api/animals/
    body {
          "name": "TOO",
          "age": 1,
          "weight": 20,
          "sex": "macho",
          "group": {
            "name": "cao",
            "scientific_name": "canis familiaris"
          },
          "characteristics": [
            {
              "name": "peludo"
            },
            {
              "name": "medio porte"
            },
						 {
              "name": "bravo"
            }
          ]
        }
 

```
```Python
    Response
    {
  "id": 5,
  "name": "TOO",
  "age": 1.0,
  "weight": 20.0,
  "sex": "macho",
  "group": {
    "id": 3,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristics": [
    {
      "id": 4,
      "name": "peludo"
    },
    {
      "id": 5,
      "name": "medio porte"
    },
    {
      "id": 6,
      "name": "bravo"
    }
  ]
}

```
## GET - Listando todos os animais
```Python
    get : localhost:8001/api/animals/

```

```Python
    response
    [
  {
    "id": 2,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 3,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": []
  },
  {
    "id": 3,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 3,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "id": 4,
        "name": "peludo"
      }
    ]
  },
  {
    "id": 4,
    "name": "Bidu",
    "age": 1.0,
    "weight": 30.0,
    "sex": "macho",
    "group": {
      "id": 3,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "id": 4,
        "name": "peludo"
      }
    ]
  },
  {
    "id": 5,
    "name": "TOO",
    "age": 1.0,
    "weight": 20.0,
    "sex": "macho",
    "group": {
      "id": 3,
      "name": "cao",
      "scientific_name": "canis familiaris"
    },
    "characteristics": [
      {
        "id": 4,
        "name": "peludo"
      },
      {
        "id": 5,
        "name": "medio porte"
      },
      {
        "id": 6,
        "name": "bravo"
      }
    ]
  }
]
    
```

## GEL - Listando animal por id

```Python
    get : localhost:8001/api/animals/2

```

```Python
    response
    {
  "id": 2,
  "name": "Bidu",
  "age": 1.0,
  "weight": 30.0,
  "sex": "macho",
  "group": {
    "id": 3,
    "name": "cao",
    "scientific_name": "canis familiaris"
  },
  "characteristics": []
}

```

## DELETE - Excluindo um animal

```Python
    delete : localhost:8001/api/animals/1/

```

```Python
    response
    No contente 204
```
