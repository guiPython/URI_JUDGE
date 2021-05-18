using System;
using System.Threading.Tasks;
using System.Collections;
using System.Diagnostics;

class URI
{
    public static int Limit = 2000001;
    public static BitArray Sieve = new BitArray(Limit, true);
    public static int[] Dividers = new int[Limit], HiperPrimesQtd = new int[Limit];
    static void Main()
    {
        HiperPrimes();

        int number;
        bool status = int.TryParse(Console.ReadLine(), out number);
        while (status)
        {
            Console.WriteLine(HiperPrimesQtd[number]);
            status = int.TryParse(Console.ReadLine(), out number);
        }

    }

    static void HiperPrimes()
    {
        int dividersQTD, aux;
        for (int i = 2; i < Limit; i++)
        {
            if (Sieve.Get(i))
            {
                Dividers[i] = 2;
                for (int j = i + i; j < Limit; j += i)
                {
                    Sieve.Set(j, false);
                    dividersQTD = 0;
                    aux = j;

                    while (aux % i == 0)
                    {
                        aux /= i;
                        dividersQTD++;
                    }

                    if (Dividers[j] == 0) Dividers[j] = dividersQTD + 1;
                    else Dividers[j] *= (dividersQTD + 1);
                }
            }
        }

        HiperPrimesQtd[1] = 0;

        for (int x = 2; x < Limit; x++)
        {
            HiperPrimesQtd[x] = HiperPrimesQtd[x - 1];
            if (Sieve.Get(Dividers[x])) HiperPrimesQtd[x]++;
        }

    }
}