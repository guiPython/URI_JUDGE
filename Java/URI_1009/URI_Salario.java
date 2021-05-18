package URI_1009;

import java.util.Scanner;

public class URI_Salario {
    public static void main(String[] args) {
        final Scanner input = new Scanner(System.in);
        // Usar entrada de decimais separadas por virgula
        final String nome = input.next();
        final Float salario = input.nextFloat();
        final Float montante = input.nextFloat();

        System.out.printf("TOTAL = R$ %.2f", salario + 0.15 * montante);
    }
}