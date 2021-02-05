#nullable enable
using System;
using Gtk;

namespace interface_commander
{
    static class Program {
 
        static void Main()
        {
            Application.Init ();

            Button btn = new Button("Hello world");
            btn.Clicked += Hello;
 
            Window window = new Window ("helloWorld");
            window.DeleteEvent += Delete_event;
        
            window.Add(btn);
            window.ShowAll();
        
            Application.Run ();
 
        }

        private static void Delete_event(object obj, DeleteEventArgs args)
        {
            Application.Quit();
        }

        private static void Hello(object? obj, EventArgs args)
        {
            Console.WriteLine("Hello World");
            Application.Quit();
        }
    }
}