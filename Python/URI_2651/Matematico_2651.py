def Matematico(op):
    for x in range(int(op[2]),11):
        if op[0] != op[2]:
            print("{} x {} = {} && {} x {} = {}".format(op[0],x,int(op[0])*x,op[2],op[2],int(op[2])*x))
        else:
            print("{} x {} = {}".format(op[0],op[2],int(op[2])*x))


def main():
    qtd =  int(input())
    for x in range(qtd):
        op = input()
        Matematico(op)
main()