# A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. 
# Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 
# Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def imparmult (n):
    if n % 2 == 0:
        return "Somente número impar"
    if n == 1:
        return 1
    
    return n * imparmult(n-2)


print(imparmult(7))  