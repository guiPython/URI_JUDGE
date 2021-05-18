using System;

class Quadrado_de_Pares {
    public static void Main(){
        var lim = Int32.Parse(Console.ReadLine());
        for ( var i = 2 ; i <= lim ; i+=2){
            Console.WriteLine(String.Format("{0}^{0} = {1}",i,Math.Pow(i,2)));
        }
        Console.ReadLine();
    }
}