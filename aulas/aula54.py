"""
Exercicio lista de compras

Crie uma lista de compras com nome dos produtos e quantidades.

Pergunte ao usuário para adicionar novos produtos e quantidades.

A cada novo item adicionado, exiba a lista de compras atualizada.

O usuário poderá apagar um item da lista de compras.

O usuário poderá excluir toda a lista de compras.

O usuário poderá ver a quantidade de itens na lista de compras.
"""

lista_compras = []

def adicionar_item():
    nome_produto = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    item = {"nome": nome_produto, "quantidade": quantidade}
    lista_compras.append(item)
    print("Item adicionado com sucesso!")
    print_lista_compras()

def print_lista_compras():
    print("Lista de compras:")
    for item in lista_compras:
        print(f"{item['nome']} - {item['quantidade']} unidades")

def excluir_item():
    print_lista_compras()
    item_excluido = input("Digite o nome do item que deseja excluir: ")
    for item in lista_compras:
        if item["nome"] == item_excluido:
            lista_compras.remove(item)
            print("Item excluido com sucesso!")
            print_lista_compras()
            return
    print("Item nao encontrado na lista.")
    print_lista_compras()

def excluir_lista():
    lista_compras.clear()
    print("Lista excluida com sucesso!")
    print_lista_compras()

while True:
    print("Selecione uma opção:")
    print("1 - Adicionar item")
    print("2 - Ver lista de compras")
    print("3 - Excluir item")
    print("4 - Excluir lista")
    print("5 - Sair")
    opcao = input("Opcão: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        print_lista_compras()
        print(f"Quantidade de itens: {len(lista_compras)}")
    elif opcao == "3":
        excluir_item()
    elif opcao == "4":
        excluir_lista()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

    print()



print_lista_compras()