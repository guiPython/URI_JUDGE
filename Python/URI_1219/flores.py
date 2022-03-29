from functools import reduce
from math import pi
from typing import List

def area_triangulo(lados: List[int]) -> dict:
    semi_p = reduce(lambda acc, val: acc + val, lados, 0) / 2
    area   = reduce(lambda acc, val: acc * (semi_p - val),lados,semi_p) ** 0.5
    return {'area' : area, 'semi_p': semi_p}

def area_circulo_interno(dados_triangulo: dict) -> float:
    return pi * (dados_triangulo['area'] / dados_triangulo['semi_p'])**2

def area_circulo_externo(lados: List[int], area_triangulo: float) -> float:
    produto_lados = reduce(lambda acc, val: acc * val, lados,1)
    return pi * (produto_lados / (4 * area_triangulo))**2


def main():

    while True:
        try:
            lados = [int(valor) for valor in input().split(" ")]

            dados_violeta = area_triangulo(lados) 
            area_rosa = area_circulo_interno(dados_violeta)
            area_violeta = dados_violeta['area'] - area_rosa
            area_amarela = area_circulo_externo(lados, dados_violeta['area']) - (area_rosa + area_violeta)

            print(f'{area_amarela:.4f} {area_violeta:.4f} {area_rosa:.4f}')
            
        except EOFError:
            break
    

main()