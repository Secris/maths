using System.Linq.Expressions;

/*
    Start with x
    If x is odd 3x+1
    If x is even x/2
*/


string user_input = "";
int x = 0;
List<int> calculated = new List<int>();

// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, please supply a starting number");
user_input = Console.ReadLine() ?? "";

if((user_input != "") && int.TryParse(user_input, out x)) {
    Console.WriteLine("Got it starting with: " + x);
    calculated.Add(x);
    do {
        if(x % 2 == 0) {
            x = x / 2;
        } else {
            x = (3 * x) + 1;
        }

        calculated.Add(x);
    } while(x > 1);

    string results = string.Join(", ", calculated);
    Console.WriteLine($"Results: {results}");
}
else {
    Console.WriteLine("There seems to have been an error");
}
