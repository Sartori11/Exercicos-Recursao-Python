# 4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 

def somaLista(lista):
    if lista == []:
        return 0
    return lista[0] + somaLista(lista[1:]) # 1: tira o primeiro termo e pega a  lista a partir do proximo

print(somaLista([1,2,3]))

