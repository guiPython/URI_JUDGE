package URI_1040;

import java.util.Scanner;

public class Media_3 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        String[] notas = input.nextLine().split(" ");
        Double media = media(notas);
        System.out.printf("Media: %.1f\n",media);

        if (media <= 5.0){
            System.out.println("Aluno Reprovado.");
        }

        else if ( media >= 7.0){
            System.out.println("Aluno Aprovado.");
        }

        else{
            System.out.println("Aluno em Exame.");
            Double nota_rec = input.nextDouble();
            System.out.println("Nota do Exame: " + nota_rec);
            mediaRec(media,nota_rec);
        }
    }

    public static Double media(String[] notas){
        Double media = 0.0;
        Double [] pesos = {0.2,0.3,0.4,0.1};

        for(int i = 0 ; i <= 3 ; i++){
            media += Double.parseDouble(notas[i]) * pesos[i] ;
        }

        return media;
    }

    public static void mediaRec(Double media , Double rec){
        Double mediaRec = (media + rec) / 2.0 ; 
        if (mediaRec >= 5.0){
            System.out.println("Aluno Aprovado.");
        }
        else{
            System.out.println("Aluno Reprovado.");
        }
        System.out.println("Media Final: " + mediaRec);
    }

}