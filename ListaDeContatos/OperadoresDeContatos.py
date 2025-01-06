
contatos = {}

class OperadoresDeContatos:

    def __init__(self):
        pass

    def AdicionarContato():
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        contatos[nome] = telefone
        print("Contato adicionado com sucesso!")

    def BuscarContato():
        nome = input("Digite o nome do contato: ")
        if nome in contatos:
            print(f"Nome: {nome}, Telefone: {contatos[nome]}")
        else:
            print("Contato não encontrado.")    

    def RemoverContato():
        nome = input("Digite o nome do contato: ")
        if nome in contatos:
            del contatos[nome]
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")

    def ExibirContatos():
        if contatos:
            print("Lista de contatos:")
            for nome, telefone in contatos.items():
                print(f"Nome: {nome}, Telefone: {telefone}")
        else:
            print("Nenhum contato encontrado.")
    
    def sair():
        print("Saindo...")
        exit()