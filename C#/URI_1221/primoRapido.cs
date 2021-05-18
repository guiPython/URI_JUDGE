using System;
using System.Threading.Tasks;

class URI
{
    static void Main()
    {
        int number;
        int nCases = int.Parse(Console.ReadLine());
        for (int i = 0; i < nCases; i++)
        {
            number = int.Parse(Console.ReadLine());

            if (Prime(number)) Console.WriteLine("Prime");
            else Console.WriteLine("Not Prime");

        }
    }

    static bool Prime(int number)
    {
        if (number < 2) return false;
        if (number == 2 || number == 3 || number == 5 || number == 7) return true;
        if (number % 2 == 0 || number % 3 == 0 || number % 5 == 0 || number % 7 == 0) return false;

        int[] odds = { 13, 17, 9, 11 };
        int i = 0;
        Task<bool>[] tasks = new Task<bool>[4];
        double limit = Math.Sqrt(number);

        foreach (int odd in odds)
        {
            tasks[i] = Task.Factory.StartNew(() => LoopPrime(number, limit, odd));
            i++;
        }

        Task.WaitAll(tasks);

        foreach (Task<bool> task in tasks)
        {
            if (!task.Result) return false;
        }

        return true;
    }

    static bool LoopPrime(int number, double limit, int digit)
    {
        for (int i = digit; i < limit; i += 10)
        {
            if (number % i == 0) return false;
        }

        return true;
    }
}