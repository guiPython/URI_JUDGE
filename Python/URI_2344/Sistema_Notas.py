def notas(numero):
    if numero == 0: nota = "E"

    elif numero <= 35: nota = "D"

    elif numero <= 60: nota = "C"

    elif numero <= 85: nota = "B"

    else: nota = "A"

    return nota

def main():
    numero = int(input())
    print(notas(numero))
main()