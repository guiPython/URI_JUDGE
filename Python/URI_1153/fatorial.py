
def fatorial(numero: int) -> int:
    resultado = 0
    while numero >=1:
        resultado *= numero
        numero -= 1
    return resultado

def main():
    print(fatorial(int(input())))
main()