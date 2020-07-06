# Gerar lista de primos [2:N] Crivo de Erastoteles
# Condicao 1 todo primo e hiperprimo
# Decomposicao em Fatores primos se a qtd de fatores estiver no vetor temos um hiperprimo

def crivo_erastoteles(DIM):
    vals=[True]*DIM
 
# Os números 0 e 1 não são considerados primos
    vals[0]=False
    vals[1]=False
 
# Percorrer a lista à procura de um número primo
    for i in range(2,DIM+1):
    # Se for primo, percorre-se toda a lista e tiram-se os múltiplos
        if vals[i]:
            for j in range(i*i,DIM,i):
                vals[j]=False
    return vals

print(crivo_erastoteles(10))