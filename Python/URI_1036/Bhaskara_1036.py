def Bhaskara(A,B,C):
    delta = B**2 - 4*A*C
    if delta < 0 or A == 0 :
        print("Impossivel Calcular")
    else:
        print("R1 = {}".format((-B + delta**0.5)/(2*A)))
        print("R2 = {}".format((-B - delta**0.5)/(2*A)))

def main():
    A,B,C = input().split(" ")
    Bhaskara(float(A),float(B),float(C))
main()