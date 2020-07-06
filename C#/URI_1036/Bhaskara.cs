using System;
using System.Linq;

class Bhaskara{
    public static void Main(string[] args ){

        string valores = Console.ReadLine();
        var list_val = valores.Split(" ").Select(double.Parse).ToList();
        double delta = Math.Pow(list_val[1],2) - (4 * list_val[0] * list_val[2]); 
        
        if ( delta > 0 & list_val[0] != 0) {
            Console.WriteLine(String.Format("R1 = {0}",(-list_val[1]+Math.Pow(delta,0.5))/(2*list_val[0])));
            Console.WriteLine(String.Format("R2 = {0}",(-list_val[1]-Math.Pow(delta,0.5))/(2*list_val[0])));
        }

        else{
            Console.WriteLine("Impossivel Calcular");
        }
    }
}