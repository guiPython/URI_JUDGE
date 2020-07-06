def main():
    val = list(int(input()) for x in range(0,4))
    resultado = (val[0]*val[1]-val[2]*val[3])
    print(f'DIFERENCA = {resultado}')
main()