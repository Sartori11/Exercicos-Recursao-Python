#RECURSAO É PILHA DE PRATO , O ULTIMO A CHEGAR É O PRIMEIRO A SAIR

# Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.


# criterio de parada => chegar no 1
def fat (n):
    if n <= 0:
        return 1
    return n * fat(n-1)        # n = 4 ->4 *fat(3) -> 3*fat(2) -> 2*fat(1) - > 1* 1 (fat(0) return 1)  <- e depois desempilha

        
print(fat(4))
