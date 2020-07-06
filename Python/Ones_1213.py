def main():
    while True:
        try:
            numero = int(input())
            contador , divisor = 1 , 1
            while divisor % numero != 0 :
                divisor = ( 10*divisor + 1) % numero 
                contador += 1
            print(contador)
        except EOFError:
            break
main()