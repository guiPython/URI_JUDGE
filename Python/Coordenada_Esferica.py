from math import sin , cos , atan , acos , degrees
from functools import reduce
Coordenadas1 = [0,0,-2,1.414214,1.414214,0]
Coordenadas2 = [2.819078,0.991098,0.265564,2.457456,1.474953,0.886241]
tempo = 2
raio = lambda coord_f: reduce(lambda x,y: x + y ,list(map(lambda x: x**2 ,coord_f)))**0.5
dp = lambda Coordenadas : reduce(lambda x,y: x+y ,[(x-y)**2 for x in Coordenadas[3:] for y in Coordenadas[0:3]])**0.5

# Encontrar Theta e phi 
Theta1 = atan(0) ; Theta2 = atan(1)
Phi1 = acos(-1)
Phi2 = acos(0.265564/raio(Coordenadas2[0:3]))
print(degrees(Theta1)) 
print(degrees(Theta2))
print(Phi1)
Theta_f = (Theta2 - Theta1 )*tempo
print(degrees(Theta_f))
zf1 = cos(Phi1) * 2 + Coordenadas1[2] 
zf2 = cos(Phi2) * raio(Coordenadas2[0:3]) + Coordenadas2[2] + Coordenadas2[5]
print(zf1)
print(zf2)
print(acos(-1))
print(cos(acos(-1)))