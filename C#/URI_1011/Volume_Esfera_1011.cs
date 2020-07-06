
using System;
    
class Program{
    static void Main(){

    double r = Double.Parse(Console.ReadLine());

    Func <double,double> Volume_Esfera = raio => 3.14159 * 4/3 *raio*raio*raio;
    
    Console.WriteLine (Math.Round(Volume_Esfera(r),3));

        }
    
}