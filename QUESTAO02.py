lista = []

def listar():
    for i in range(10):
        item = str(input("Digite a tarefa a ser listada: "))
        lista.append(item)


listar()
print("A lista de tarefas é: ")
for j in range (10):
    print(lista[j])
