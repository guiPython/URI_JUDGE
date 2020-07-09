
deslocameto = lambda v,t: v*2*t 

def main():
    while True:
        v_t = [int(x) for x in input().split()]
        if v_t == []: break
        else:
            print(deslocameto(v_t[0],v_t[1]))
main()