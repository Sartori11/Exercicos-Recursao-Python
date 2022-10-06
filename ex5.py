#5) Crie uma função recursiva que receba um número inteiro positivo N e calcule o somatório dos números de 1 a N. 

def soma(n): 
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return soma(n-1) + (n)
        
    
        
print(soma(4))