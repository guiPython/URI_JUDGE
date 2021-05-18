using System;
using System.Globalization; 

class URI {
    static void Main(string[] args) { 

        string[] p1 = Console.ReadLine().Split(' ');
        string[] p2 = Console.ReadLine().Split(' ');
        double vP1 = int.Parse(p1[1]) * double.Parse(p1[2],CultureInfo.InvariantCulture);
        double vP2 = int.Parse(p2[1]) * double.Parse(p2[2],CultureInfo.InvariantCulture);
        System.Console.WriteLine("VALOR A PAGAR: R$ " + (vP1 + vP2).ToString("F2",CultureInfo.InvariantCulture));
    }

}