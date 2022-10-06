# 14) Faça uma função recursiva que receba um número inteiro positivo par N e 
# imprima todos os números pares de 0 até N em ordem crescente.


def antcpar (n):
    if n == 2:
        return [2,]
    
    return antcpar(n-2) + [n,]



print(antcpar(10))