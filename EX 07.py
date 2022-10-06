# Crie um programa em python que receba um vetor de números reais com 100 elementos. 
# Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 

import math
def inverterVetor (vetor,k):
    if (math.ceil(len(vetor)/2) == k): 
        return vetor
    pos_troca = len(vetor) - k
    aux = vetor[pos_troca]
    vetor[pos_troca] = vetor[k-1] 
    vetor[k-1] = aux
    return   inverterVetor(vetor,k)  


vetor = [1,2,7,5,7]
print(inverterVetor(vetor,len(vetor)))




def inverterVetor2 (vetor,k=0):
    if (math.ceil(len(vetor)/2) == k): 
        return vetor
    var = (k+1)*(-1)
    aux = vetor[k]
    vetor[k] = vetor[var] 
    vetor[var] = aux
    return   inverterVetor(vetor,k+1)  


vetor = [1,2,7,5,7]
print(inverterVetor(vetor))
