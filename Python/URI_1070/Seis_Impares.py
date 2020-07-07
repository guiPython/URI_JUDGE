numero = int(input())
aux = 0
while aux < 6:
    if numero % 2 != 0:
        print(numero)
        aux += 1
    numero += 1