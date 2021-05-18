using System;
using System.Threading.Tasks;
using System.Linq;
using System.Collections.Generic;

class SuperPrimoEX
{
    static void Main()
    {
        string numberS = Console.ReadLine();

        while (!string.IsNullOrEmpty(numberS))
        {
            long numberI = long.Parse(numberS);
            if (Primo(numberI))
            {
                if (SuperPrimo(numberS)) Console.WriteLine("Super");
                else Console.WriteLine("Primo");
            }
            else Console.WriteLine("Nada");
            numberS = Console.ReadLine();
        }

    }

    static bool Primo(long n)
    {
        if (n < 2) return false;
        if (n == 2 || n == 3 || n == 5 || n == 7) return true;
        if (n % 3 == 0 || n % 2 == 0 || n % 5 == 0) return false;

        int[] numbers = { 11, 9, 7, 3 };
        int i = 0;

        double limit = Math.Ceiling(Math.Sqrt(n));

        Task<bool>[] tasks = new Task<bool>[4];

        foreach (int number in numbers)
        {
            tasks[i] = Task<bool>.Factory.StartNew(() => { return Loop(n, number, limit); });
            i++;
        }

        Task.WaitAll(tasks);

        foreach (Task<bool> task in tasks)
        {
            if (!task.Result) return false;
        }

        return true;
    }

    static bool SuperPrimo(string n)
    {
        for (int i = 0; i < n.Length; i++)
        {
            if (!Primo((int)(Char.GetNumericValue(n[i])))) return false;
        }
        return true;
    }

    static bool Loop(long test, int n, double limit)
    {
        for (int i = n; i <= limit; i += 10)
        {
            if (test % i == 0) return false;
        }
        return true;
    }


}