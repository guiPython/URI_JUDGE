#Unicode Letras 97 - 122 || a - z
def Decodifica (n_letras):
    while n_letras > 0:
        codigo = input().split(" ")
        letra = chr(96 + len(codigo[0]) + 3*(len(codigo) - 1))
        print(letra) ; n_letras -= 1
    

def main():
    while True:
        try:
            n_letras = int(input())
            Decodifica(n_letras)
        except EOFError:
            break
        except ValueError:
            break
main()
