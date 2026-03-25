# Classe de carros
class Carro:
    def __init__(self, marca, modelo, ano, versao, cor, categoria):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.versao = versao
        self.cor = cor
        self.categoria = categoria


# Sistema principal
def main():
    carros = []

    # Loop do sistema
    while True:
        print("\nBem vindo ao Cadastro de carro! Digite uma das opções abaixo: ")
        print("1 - Cadastrar veiculo")
        print("2 - Listar veiculo")
        print("3 - Remover carro da lista")
        print("4 - Sair")

        try:
            opcao = int(input("Digite: "))
        except ValueError:
            print("Digite um número válido!")
            continue

        # Cadastro de carros
        if opcao == 1:
            try:
                marca = input("Digite a marca do carro: ")
                modelo = input("Digite o modelo do carro: ")
                ano = int(input("Digite o ano do carro: "))
                versao = input("Digite versão do carro: ")
                cor = input("Digite a cor do carro: ")
                categoria = input("Digite a categoria do carro: ")

                carro = Carro(marca, modelo, ano, versao, cor, categoria)
                carros.append(carro)

                print("Carro cadastrado com sucesso!")

            except ValueError:
                print("Digite um número válido para o ano!")

        # Listagem
        elif opcao == 2:
            if not carros:
                print("Nenhum carro cadastrado!")
            else:
                for i, c in enumerate(carros, 1):
                    print(f"{i} - {c.marca} {c.modelo} ({c.ano}) | {c.cor} | {c.categoria}")

        # Remoção
        elif opcao == 3:
            if not carros:
                print("Nenhum carro cadastrado!")
            else:
                for i, c in enumerate(carros, 1):
                    print(f"{i} - {c.marca} {c.modelo} ({c.ano})")

                try:
                    deletar = int(input("Digite o número do carro para deletar: "))
                    indice = deletar - 1

                    if 0 <= indice < len(carros):
                        carros.pop(indice)
                        print("Carro removido com sucesso!")
                    else:
                        print("Número inválido!")

                except ValueError:
                    print("Digite um número válido!")

        # Sair
        elif opcao == 4:
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()