import requests

# URL do recurso
url = "https://jsonplaceholder.typicode.com/posts"

# Exemplo 1: Requisição GET
response_get = requests.get(url)
print("GET Response:")
print(response_get.status_code)  # Código de status
print(response_get.json())       # Conteúdo da resposta em JSON

# Exemplo 2: Requisição POST (enviando dados)
dados_post = {
    "title": "Título de Exemplo",
    "body": "Corpo do texto da postagem.",
    "userId": 1
}
response_post = requests.post(url, json=dados_post)
print("\nPOST Response:")
print(response_post.status_code)
print(response_post.json())

# Exemplo 3: Requisição PUT (atualizar recurso)
url_put = f"{url}/1"  # Atualizar o post com ID 1
dados_put = {
    "title": "Título Atualizado",
    "body": "Texto atualizado da postagem.",
    "userId": 1
}
response_put = requests.put(url_put, json=dados_put)
print("\nPUT Response:")
print(response_put.status_code)
print(response_put.json())

# Exemplo 4: Requisição DELETE
url_delete = f"{url}/1"  # Deletar o post com ID 1
response_delete = requests.delete(url_delete)
print("\nDELETE Response:")
print(response_delete.status_code)  # Deve retornar 200 ou 204
