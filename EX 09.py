# Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 

def soma (n):
    if n == 1:
        return 1
    return  n + soma(n-1)
    
print(soma(5))
