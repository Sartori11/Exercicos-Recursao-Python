# 3) Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 

def inverter(n,k=0):
    if n <=9:
        return k + n
    k = k * 10 + n % 10 * 10
    return inverter(n // 10, k)

print(inverter(12))
