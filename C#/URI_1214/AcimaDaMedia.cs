using System; 
using System.Globalization;
class URI {

    static void Main(string[] args) { 

        int n = int.Parse(Console.ReadLine());
        string[] percent = new string[n]; 

        for(int i = 0; i < n; i++){
            int[] array = Array.ConvertAll(Console.ReadLine().Split(' '),int.Parse);
            int nTAlunos = array[0]; int nTAMAlunos = 0; double mediaG = 0.0;
            for(int j = 1; j <= nTAlunos; j++ ) mediaG += array[j];
            for(int k = 1; k <= nTAlunos; k++ ) if( array[k] > mediaG/nTAlunos ) nTAMAlunos+=1;
            percent[i] =  ( (double) nTAMAlunos * 100.00 / nTAlunos ).ToString("F3") + "%";
        }

        foreach(string p in percent) System.Console.WriteLine(p);
    }

}