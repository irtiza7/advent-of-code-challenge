using System;
using System.IO;

string fileContentsString = "";
string inputFile = @"./inputt.txt";

if (File.Exists(inputFile))
{
    fileContentsString = readAndConvertFileContentsToString(inputFile);
}
else
{
    Console.WriteLine($"Couldn't find file named: {inputFile.TrimStart("./".ToCharArray())}");
    return;
}

Console.WriteLine("hui");
int[] indexesToExamine = { 1, 9, 10, 11 };
string partNumber = "";
int sum = 0;
for (int i = 0; i < fileContentsString.Length; i++)
{
    if (Char.IsDigit(fileContentsString[i]))
    {
        partNumber += fileContentsString[i];

        foreach (int index in indexesToExamine)
        {
            if ((i + index) > fileContentsString.Length - 1)
            {
                break;
            }

            if (isSymbol(fileContentsString[i + index]))
            {
            }

        }
    }
    else if (isSymbol(fileContentsString[i]))
    {
        continue;
    }
    else if (fileContentsString[i] == '.')
    {
        partNumber = "";

        int num;
        if (Int32.TryParse(partNumber, out num))
        {
            Console.WriteLine(partNumber);
            sum += num;
            partNumber = "";
        }
    }
}



string readAndConvertFileContentsToString(string fileName)
{
    string[] lines = File.ReadAllLines(fileName);

    string content = "";
    foreach (string line in lines)
    {
        content += line;

    }
    return content;
}

static bool isSymbol(char ch)
{
    string symbols = @"/@#!$%^&*()+-";
    return symbols.Contains(ch) ? true : false;
}