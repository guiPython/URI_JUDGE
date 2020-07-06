using System;

class Primo{
    public static void Main ( string [] args){
        int rept = Int32.Parse(Console.ReadLine());
        for ( var x = 0 ; x < rept ; x++){
            var n = Int32.Parse(Console.ReadLine());
            Console.WriteLine(Verifica_Primo(n));
        }
    }

    private static string Verifica_Primo(int numero){
        if (numero > 2 & numero % 2 ==0){
            return(String.Format("{0} nao eh primo",numero));
        }
        else{
            for(var x = 3 ; x < (Math.Pow(numero,0.5)+1);x+=2){
                if ((numero % x) == 0){
                    return(String.Format("{0} nao eh primo",numero));
                }
            }
        }
        return (String.Format("{0} eh primo",numero));
    }
}