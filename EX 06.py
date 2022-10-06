#6) Crie um programa em C, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule kn . 
# Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 

# 2^3 = 2*2*2*2

def potencia(k,n):
    if n == 0:
        return 1
    else:
        return potencia(k,n-1) * k


print(potencia(2,4))
