from produto import Produto
produtos = {}
total_geral = 0
while True:
    print("1 - Adicionar produto")
    print("2 - Ver lista")
    print("3 - Alterar produto")
    print("4 - Remover produto")
    print("5 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números!")
        continue

    if opcao == 1:
        nome = str(input("Nome do produto: ")) #as variaveis do objeto em "self"
        marca = str(input("Marca do produto: "))
        quantidade = float(input("Quantidade: "))
        preco_unitario = float(input("Preço do produto: "))

        produto = Produto(nome, marca, quantidade, preco_unitario)
        produtos[produto.id] = produto
        print("Produto adicionado com sucesso! ")
    elif opcao == 2:
        print("\nLista de produtos:")
        for p in produtos.values():
            print(p, "- Total: R$", p.total())
    elif opcao == 3:
        for p in produtos.values():
            print(p)
        alterar = int(input("\nQual produto deseja alterar?"))
        for i in produtos.values():
            if i == alterar:
                pass
    elif opcao == 4:
        pass
    elif opcao == 5:
        print("Saindo..")
        break