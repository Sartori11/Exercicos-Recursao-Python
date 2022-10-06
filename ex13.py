
# Faça uma função recursiva que receba um número inteiro positivo N e 
# imprima todos os números naturais de 0 até N em ordem decrescente. 

def antd (n):
    if n == 0:
        return [0,]    
    return [n,] + antd(n-1)






print(antd(5))