//Assignment 9
//A program to implement a timer with multiple threads.
using System;  
using System.Collections.Generic;  
using System.Text;  
using System.Threading;  
  
namespace Clock_MultiThreading  
{  
    class Program  
    {  
        static void Main(string[] args)  
        {  
            Console.WriteLine("Welcome to Timer Clock Multithread Program\t By Sarah Hussain");  
            Console.SetCursorPosition(03, 08);  //set the cursor position  
            Console.Write("12 hour clock in ");  //set clock type 12hrs or 24hrs i set here 12 hrs clock  
            Console.SetCursorPosition(20, 08);  
            Console.WriteLine("hr:min:sec:M.Sec");  
            Console.Beep();  
            for (int hr = 0; hr <= 11; hr++)  // Apply  for loop for hour  
            {  
                for (int min = 0; min <= 59; min++)    // Apply  for loop for min  
                {  
                    for (int sec = 0; sec <= 59; sec++)  // Apply  for loop for sec  
                    {  
                        for (int Msec = 0; Msec < 99; Msec++)  // Apply  for loop for Msec  
                        {  
                            if (hr < 10)         //Apply if condition for hour  
                            {  
                                if (min < 10)      //Apply if condition for min  
                                {  
                                    if (sec < 10)    //Apply if condition for sec  
                                    {  
                                        Console.SetCursorPosition(18, 10);  
                                        Console.Write("[ 0{0}: 0{1}: 0{2}:{3} ]", hr, min, sec, Msec);  
                                        Thread.Sleep(10); //apply thread with time sleep  
                                    }  
                                    else if (sec >= 10)  
                                    {  
                                        Console.SetCursorPosition(18, 10);  
                                        Console.Write("[ 0{0}: 0{1}: {2}:{3} ]", hr, min, sec, Msec);  
                                        Thread.Sleep(10);  //apply thread with time sleep  
                                    }  
                                }  
                                else if (min >= 10)  
                                {  
                                    if (sec < 10)  
                                    {  
                                        Console.SetCursorPosition(18, 10);  
                                        Console.Write("[ 0{0}: {1}: 0{2}:{3} ]", hr, min, sec, Msec);  
                                        Thread.Sleep(10);   //apply thread with time slep  
                                    }  
                                    else if (sec >= 10)  
                                    {  
                                        Console.SetCursorPosition(18, 10);  
                                        Console.Write("[ 0{0}: {1}: {2}:{3} ]", hr, min, sec, Msec);  
                                        Thread.Sleep(10);   //apply thread with time sleep  
                                    }  
                                }  
                            }  
                            else if (hr >= 10)  
                            {  
                                if (min < 10)  
                                {  
                                    if (sec < 10)  
                                    {  
                                        Console.SetCursorPosition(20, 10);  
                                        Console.Write("{0}:0{1}:0{2}:{3}", hr, min, sec, Msec);  
                                        Thread.Sleep(10);  //apply thread with time sleep  
                                    }  
                                    else if (sec >= 10)  
                                    {  
                                        Console.SetCursorPosition(20, 10);  
                                        Console.Write("{0}:0{1}:{2}:{3}", hr, min, sec, Msec);  
                                        Thread.Sleep(10);  //apply thread with time sleep  
                                    }  
                                }  
                                else if (min >= 10)  
                                {  
                                    if (sec < 10)  
                                    {  
                                        Console.SetCursorPosition(20, 10);  
                                        Console.Write("{0}:{1}:0{2}:{3}", hr, min, sec, Msec);  
                                        Thread.Sleep(10);  //apply thread with time sleep  
                                    }  
                                    else if (sec >= 10)  
                                    {  
                                        Console.SetCursorPosition(20, 10);  
                                        Console.Write("{0}:{1}:{2}:{3}", hr, min, sec, Msec);  
                                        Thread.Sleep(10);  //apply thread with time sleep  
                                    }  
                                }  
                            }  
                        }  
                        Console.Beep();  
                    }  
                    Console.Beep(); Console.Beep();  
                }  
            }  
            Console.ReadKey();  
        }  
    }  
}  
