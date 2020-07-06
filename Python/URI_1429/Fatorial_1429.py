fatorial = lambda numero : 1 if numero<1 else numero*fatorial(numero-1)

def ACM_DEC(numero):
    aux = 1 ; dec = 0
    for x in numero[::-1]:
        dec += int(x) * fatorial(aux)
        aux += 1
    return dec

def main():
    while True:
        num_ACM = str(input().strip())
        if num_ACM == '0':
            break
        else: print(ACM_DEC(num_ACM))
main()