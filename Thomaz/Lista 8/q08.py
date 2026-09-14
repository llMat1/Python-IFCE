tarefas = []
for i in range(3):
    tarefa = input(f"Digite a {i + 1}ª tarefa: ")
    tarefas.append(tarefa)

print("\nTodas as tarefas cadastradas:")
for t in tarefas:
    print(f"- {t}")