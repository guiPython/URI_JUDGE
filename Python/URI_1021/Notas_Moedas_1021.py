def notas_moedas(valores):

    val_int = int(valores[0]) ; val_dec = int(valores[1])
    notas_moedas = [100,50,20,10,5,2,1]

    print("NOTAS:")

    for nota in notas_moedas[:len(notas_moedas)-1]:
        qtd_notas = val_int // nota
        val_int %= nota
        print("{} nota(s) de R$ {:.2f}".format(qtd_notas,nota))

    print("MOEDAS:")

    if val_int >= 1 : print("{} moeda(s) de R$ {:.2f}".format(val_int//1,1))
    else: print("0 moeda(s) de R$ {:.2f}".format(1))

    del notas_moedas[5]

    for moeda in notas_moedas[1::]:
        qtd_moedas = val_dec // moeda
        val_dec %= moeda
        print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas,moeda/100))

def main():
    valores = input().split(".")
    notas_moedas(valores)
main()