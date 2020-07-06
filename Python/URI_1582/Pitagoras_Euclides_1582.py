def mdc(n1,n2):
    while n2!=0:
        r = n1 % n2 ; n1 = n2 ; n2 = r
    return n1

def Triplas_Pitagoricas( triplas ):
    triplas.sort()
    if triplas[0]**2 + triplas[1]**2 == triplas[2]**2:
        if mdc(mdc(triplas[0],triplas[1]),triplas[2]) == 1:
            return 'tripla pitagorica primitiva'
        return 'tripla pitagorica'
    return 'tripla'

def main():
    while True:
        try:
            tripla = input().strip().split()
            tripla_int = [int(numero) for numero in tripla]
            print(Triplas_Pitagoricas(tripla_int))
        except EOFError:
            break
main()