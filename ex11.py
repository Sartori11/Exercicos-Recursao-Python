# A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. 
# Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.

# 2 x 3 = 2+ 2 +2 ou 3+ 3

def mult (x,y):
    if y == 1:
        return x
    
    return x +  mult(x,y-1)

print(mult(9,9))