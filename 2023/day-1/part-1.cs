using System;

namespace AOC
{
    class Day1_Task1{
        static void Main(string[] args)
      {
            string[] fileLines = File.ReadAllLines("./input.txt");
            long sum = 0;

            foreach (string line in fileLines)
            {
                int n1 = 0, n2 = 0;
                foreach (char ch in line)
                {
                    int parsedChar;
                    if (int.TryParse(ch.ToString(), out parsedChar))
                    {
                        n1 = n1 == 0 ? parsedChar : n1;
                        n2 = parsedChar;
                    }
                }
                sum += ((n1 * 10) + n2);
            }
            Console.WriteLine(sum);
        }
    }
}
