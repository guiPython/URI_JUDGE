import string

def array_hash(qtd_hash):
    matriz_hash = [] ;  valor = 0
    alfabeto = list(string.ascii_uppercase)
    for x in range(qtd_hash):
        hash_code = input()
        linha_hash = []
        for y in hash_code:
            linha_hash.append(y)
        matriz_hash.append(linha_hash)
    for i in range(len(matriz_hash)):
        for j in range(len(matriz_hash[i])):
            valor += alfabeto.index(matriz_hash[i][j]) + i + j
    return valor




def main():
    qtd_teste = int(input())
    for x in range(qtd_teste):
        qtd_hash = int(input())
        print(array_hash(qtd_hash))
main()