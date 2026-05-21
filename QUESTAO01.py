lista = []

for i in range(5):
    item = int(input("Digite os valores desejados: "))
    lista.append(item)


def organizar():
    menor = 0
    maior = 0
    for j in range(5):
        if lista[menor]>lista[j]:
            menor = j
        if lista[maior]<lista[j]:
            maior = j
    

    print(f"O maior valor da lista é {lista[maior]}, e o menor é {lista[menor]}!")




organizar()