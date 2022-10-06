# 12) Faça uma função recursiva que receba um número inteiro positivo N e 
# imprima todos os números naturais de 0 até N em ordem crescente. 


# 5 -  0 1 2 3 4- 5 
def antc (n):
    if n == 0:
        return [0,]
    
    return antc(n-1) + [n,]



print(antc(10))