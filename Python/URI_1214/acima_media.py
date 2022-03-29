
from typing import List
from functools import reduce

def media(dados: List[int]) -> float:
    return reduce(lambda acc,val: acc + val, dados[1::], 0) /  dados[0]

def qtd_acima_media(media: float, dados: List[int]) -> int:
    return len(list(filter(lambda valor: valor > media, dados[1::])))


def main():
    numero_testes : int = int(input())

    for _ in range(numero_testes):
        dados = [int(valor) for valor in input().split(" ")]
        aptos = qtd_acima_media(media(dados),dados)
        
        print(f'{aptos*100/dados[0]:.3f}%')
main()