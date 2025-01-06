from OperadoresDeTarefas import OperadoresDeTarefas


def ExexutarTarefas():
    while True:
        print("\nMenu:")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Remover tarefa")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            OperadoresDeTarefas.adicionar_tarefa()
        elif escolha == "2":
            OperadoresDeTarefas.listar_tarefas()
        elif escolha == "3":
            OperadoresDeTarefas.remover_tarefa()
        elif escolha == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

ExexutarTarefas()