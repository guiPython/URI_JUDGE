def main():
    n_linhas = int(input()) 
   
    s_triPascal = lambda x: 1 if x == 0 else  2**x - 1

    print(s_triPascal(n_linhas))
main()

