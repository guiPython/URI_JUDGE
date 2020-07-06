using System;
using System.Linq;
using System.Collections.Generic;

class MainClass {
  public static void Main (string[] args) {
    
    string p1 = Console.ReadLine() + " ";
    string p2 = Console.ReadLine();
    
    var coord = (p1 + p2).Split(' ').Select(double.Parse).ToList();

    Console.WriteLine(Math.Round(D_Pontos(coord),4));
    
  }
  private static double D_Pontos(List<double> coord){
    var d = Math.Pow(Math.Pow(coord[2]-coord[0],2)+Math.Pow(coord[3]-coord[1],2),0.5);
    return (d);
  }
}