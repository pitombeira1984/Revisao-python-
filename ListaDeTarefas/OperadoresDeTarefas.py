
tarefa = []
class OperadoresDeTarefas:
    def __init__(self):
        pass   

    def adicionar_tarefa():
        tarefa.append(input("Digite a tarefa: "))
        print("Tarefa adicionada com sucesso!")

    def listar_tarefas():
        if tarefa:
            print("Lista de tarefas:")
            for i, tarefas in enumerate(tarefa, start=1):
                print(f"{i}. {tarefas}")
        else:
            print("Nenhuma tarefa encontrada.")

    def remover_tarefa():
        for i, tarefas in enumerate(tarefa, start=1):
                print(f"{i}. {tarefas}")
        if tarefa:
            try:
                indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
                if 0 <= indice < len(tarefa):
                    tarefa.pop(indice)
                    print("Tarefa removida com sucesso!")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
        else:
            print("Nenhuma tarefa encontrada.")

