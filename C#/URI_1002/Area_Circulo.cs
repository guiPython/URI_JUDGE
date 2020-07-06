using System;

class Area_Circulo {
  public static void Main (string[] args) {

    double r = Double.Parse(Console.ReadLine());
    Func <double,double> Area_Circulo = raio => Math.Round(3.14159 * Math.Pow(raio,2),4);

    Console.WriteLine ("Area=" + Area_Circulo(r));
  }
}