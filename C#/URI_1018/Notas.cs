using System;

class Notas{
    public static void Main ( string[] args){

        int valor = Int32.Parse(Console.ReadLine());
        D_notas(valor);
    }

    public static void D_notas ( int valor ){
        int[] notas = new  int[] {100 ,50 , 20 , 10 , 5, 2 , 1 };
        int aux = 0;
        foreach(var x in notas){
            int qtd_notas = valor / x ;
            valor = valor % x ;
            Console.WriteLine(String.Format("{0} nota(s) de R$ {1} ",qtd_notas,notas.GetValue(aux)));
            aux++;
        }
    }
}