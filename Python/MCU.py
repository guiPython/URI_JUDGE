from functools import reduce
from math import atan , tan ,degrees
Coordenadas = [float(x) for x in input().split()] # Duas trincas de Pontos
tempo = int(input())
# Distancia entre qualquer ponto dado e a origem gera o raio de C1
raio = lambda coord_f: reduce(lambda x,y: x + y ,list(map(lambda x: x**2 ,coord_f)))**0.5
dp = lambda Coordenadas : reduce(lambda x,y: x+y ,[(x-y)**2 for x in Coordenadas[3:] for y in Coordenadas[0:3]])**0.5
#print(raio([0,0,-2]))
#print(raio([1.414214,1.414214,0]))
# Velocidade Angular d(theta) / d(t)
theta_vAng = atan(dp(Coordenadas)/raio(Coordenadas[0:3]))
print(degrees(theta_vAng))
# Velocidade Angular e theta / Unidade de tempo
# Ponto Inicial E Coordenadas[0:3]
# Ponto Inicial E Coordenadas[3:]
theta_f =theta_vAng + tempo * theta_vAng 
print(degrees(theta_f))
d_BC = tan(theta_f) * raio(Coordenadas[0:3])
print(d_BC)