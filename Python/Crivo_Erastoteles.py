import time
def crivo_de_eratostenes(n):
    numeros = [True] * (n + 1)
    
    numeros[0] = False
    numeros[1] = False
    
    primos = []
    
    for numero, primo in enumerate(numeros):
        if primo:
            primos.append(numero)
            
            for i in range(numero * 2, n + 1, numero):
                numeros[i] = False
    return primos
1
i = time.time()
primos = crivo_de_eratostenes(1500000)
f = time.time()
print(f-i)