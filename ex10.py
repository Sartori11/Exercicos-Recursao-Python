#  Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. 
# Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. 

def dig (n, k, cont = 0):
    if n < 1:
        return cont 
    
    if n == k:
        cont +=  1
    elif n % 10 == k:
        cont +=1      
    return dig(n//10,k,cont)

        

print(dig(575787252255,2))