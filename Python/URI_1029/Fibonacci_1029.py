def fibonacci(n , tabela = {}):
    global chamadas ; chamadas += 1
    if n <= 1: return n
    try: return tabela[n]
    except:
        tabela[n] = fibonacci(n-1) + fibonacci(n-2) 
        return tabela[n]

casos = int(input())
 
for x in range(casos):
    n_termo = int(input()) ; chamadas = 0
    fib = fibonacci(n_termo)
    print('fib({}) = {} calls = {}'.format(n_termo,chamadas-1,fib))
