package URI_1011;

import java.util.Scanner;

class Esfera{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Float r = input.nextFloat();
        final Float pi = 3.14159f ; 
        System.out.printf("VOLUME = %.2f" , (4/3.0) * pi * Math.pow(r, 3.0));
    }
}