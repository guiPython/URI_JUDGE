def mediana(m):
    #Verificar se Triangulo Existe
    m.sort()
    print(m)
    if m[2] >= m[1] + m[0]:
        res = -1
    else:
        # Formula de Heron
        p = sum(m) * 0.5 # Semi-Perimetro
        res = (4/3)*(p*(p-m[0])*(p-m[1])*(p-m[2]))**0.5
    return res

def main():
    while(True):
        list_med = [float(x) for x in input().split()]
        if list_med == []:
            break
        else:
            print("{:.3f}".format(mediana(list_med)))
main()