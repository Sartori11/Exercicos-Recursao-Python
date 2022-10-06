# Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente. 


def antdpar (n):
    if n == 2:
        return [2,]
    
    return [n,] + antdpar(n-2)



print(antdpar(10))