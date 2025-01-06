from OperadoresDeContatos import OperadoresDeContatos

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Buscar contato")
        print("3. Remover contato")
        print("4. Exibir contatos")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            OperadoresDeContatos.AdicionarContato()
        elif escolha == "2":
            OperadoresDeContatos.BuscarContato()
        elif escolha == "3":
            OperadoresDeContatos.RemoverContato()
        elif escolha == "4":
            OperadoresDeContatos.ExibirContatos()
        elif escolha == "5":
            OperadoresDeContatos.sair()
        else:
            print("Opção inválida. Tente novamente.")
main()