using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HacktoberFestHWcsharp
{
     public class HelloWorld
    {
        static void Main()
        {
            ConsoleColor oldColor = Console.ForegroundColor; // BG color, don't worry.
            Console.ForegroundColor = ConsoleColor.Red;

            Console.WriteLine("Hello World!");
            Console.ReadLine();

            Console.WriteLine("This is another take on the 'Hello World' program");
            Console.ReadLine();

            Console.WriteLine("It's almost like I'm becoming... Intelligent");
            Console.ReadLine();

            Console.WriteLine("Don't worry, all this is pre-writting, by some boring programmer.");
            Console.ReadLine();

            Console.WriteLine("Goodbye - Press any key to exit.");
            Console.ReadLine();
            Console.ReadKey();
        }
    }
}
