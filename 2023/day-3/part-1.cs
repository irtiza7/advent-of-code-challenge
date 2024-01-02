using System;
using System.IO;

string inputFile = @"./input.txt";
if (!File.Exists(inputFile))
{
    Console.WriteLine($"Couldn't find file named: {inputFile.TrimStart("./".ToCharArray())}");
    return;

}

int sum = 0;
string[] lines = File.ReadAllLines(inputFile);

for (int i = 0; i < lines.Length; i++)
{
    string currentline = lines[i];
    string prevLine = "";
    string nextLine = "";

    if (i - 1 >= 0)
    {
        prevLine = lines[i - 1];
    }
    if (i + 1 < lines.Length)
    {
        nextLine = lines[i + 1];
    }

    string partNumber = "";
    bool isPartNumberValid = false;
    for (int j = 0; j < currentline.Length; j++)
    {
        if (char.IsDigit(currentline[j]))
        {
            partNumber += currentline[j];

            if (isPartNumberValid)
            {
                continue;
            }

            char[] diagonalCharacters = new char[8];

            diagonalCharacters[0] = currentline.ElementAtOrDefault(j - 1);
            diagonalCharacters[1] = currentline.ElementAtOrDefault(j + 1);

            diagonalCharacters[2] = prevLine.ElementAtOrDefault(j);
            diagonalCharacters[3] = prevLine.ElementAtOrDefault(j - 1);
            diagonalCharacters[4] = prevLine.ElementAtOrDefault(j + 1);

            diagonalCharacters[5] = nextLine.ElementAtOrDefault(j);
            diagonalCharacters[6] = nextLine.ElementAtOrDefault(j - 1);
            diagonalCharacters[7] = nextLine.ElementAtOrDefault(j + 1);

            for (int k = 0; k < 8; k++)
            {
                if (isSymbol(diagonalCharacters[k]))
                {
                    isPartNumberValid = true;
                    break;
                }
            }
        }
        else
        {
            int num;
            if ((isPartNumberValid) && (Int32.TryParse(partNumber, out num)))
            {
                sum += num;
                isPartNumberValid = false;
            }
            partNumber = "";
        }

    }

    /* 
        Handle the case where the part number was at the end of line
        Since the loop will end, the last number won't have been added to the sum 
    */
    if (partNumber.Length > 0 && isPartNumberValid)
    {
        int num;
        if (Int32.TryParse(partNumber, out num))
        {
            sum += num;
        }
    }

}

Console.WriteLine($"Sum: {sum}");

bool isSymbol(char ch)
{
    string symbols = @"/@#!$%^&*()+-=";
    return symbols.Contains(ch);
}