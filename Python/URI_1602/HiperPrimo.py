from math import sqrt
import time 

def Primo(n_divisores):
    if n_divisores > 2 and n_divisores % 2 == 0:
        return False
    if n_divisores ==  2:
        return True
    else:
        for x in range(3,int(sqrt(n_divisores))+1,2):
            if n_divisores % x == 0:
                return False
    return True



def Divisores(numero):
    n_divisores = 2 # Algoritmo otimizado
    for x in range(2,int(sqrt(numero)+1)):
        if numero % x == 0 :
            if numero/x == x : n_divisores += 1
            else : n_divisores += 2
    return n_divisores



def Hiper_Primos(intervalo):
    h_primo = 0
    for x in intervalo:
        if Primo(x): h_primo +=1
        else: 
            n_divisores = Divisores(x)
            if Primo(n_divisores): h_primo += 1
    return h_primo




def main():
    inicio = time.time()
    nf_intervalo = 2000000
    intervalo = [x for x in range(2,int(nf_intervalo)+1)]
    fim = time.time()
    print(fim-inicio)
main()