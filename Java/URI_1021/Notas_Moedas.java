package URI_1021;

import java.util.Scanner;

class Main {
    public static void main(final String[] args) {
        final Scanner input = new Scanner(System.in);
        final String[] valor = input.nextLine().split(",");

        Notas(Integer.parseInt(valor[0]));
        Moedas(Integer.parseInt(valor[1]));

    }

    public static void Notas(Integer valorInt) {
        final Integer[] notas = { 100, 50, 20, 5, 2 };

        System.out.println("NOTAS:");

        for (final Integer nota : notas) {
            final Integer qtdNotas = valorInt / nota;
            valorInt %= nota;
            System.out.printf("%d nota (s) de R$ %d\n", qtdNotas, nota);
        }

        System.out.println("MOEDAS:");

        if (valorInt >= 1) {
            System.out.printf("%d moeda (s) de R$ 1.00\n", valorInt / 1);
        }
    }

    public static void Moedas(Integer valorDec) {
        final Integer[] moedas = { 50, 25, 10, 1 };

        for (final Integer moeda : moedas) {
            final Integer qtdMoedas = valorDec / moeda;
            valorDec %= moeda;
            System.out.printf("%d moeda (s) de R$ %d\n",qtdMoedas,moeda);
        }
    }
}