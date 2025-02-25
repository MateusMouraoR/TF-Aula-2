# Programa de Inventário de Produtos

# Dicionário para armazenar os produtos
inventario = {}

def adicionar_produto(nome, preco, quantidade):
    inventario[nome] = {'preço': preco, 'quantidade': quantidade}

def remover_produto(nome):
    if nome in inventario:
        del inventario[nome]
    else:
        print(f"Produto {nome} não encontrado no inventário.")

def listar_produtos():
    if inventario:
        for nome, detalhes in inventario.items():
            print(f"Nome: {nome}, Preço: R${detalhes['preço']:.2f}, Quantidade: {detalhes['quantidade']}")
    else:
        print("Inventário vazio.")

# Função principal para executar o programa
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Listar produtos")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade do produto: "))
            adicionar_produto(nome, preco, quantidade)
        elif escolha == "2":
            nome = input("Nome do produto a remover: ")
            remover_produto(nome)
        elif escolha == "3":
            listar_produtos()
        elif escolha == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa principal
if __name__ == "__main__":
    main()
