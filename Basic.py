from tkinter import*

main_window = Tk()

# Labels
Label(main_window, text="Hello World").grid(row = 0, column = 0)
Label(main_window, text= "This is Tkinter").grid(row = 1, column = 0)

# Text Input
Entry(main_window, width= 50, borderwidth= 5).grid(row = 0, column = 1)
Entry(main_window, width= 50, borderwidth= 5).grid(row = 1, column = 1)

Button(main_window, text= "Click Me").grid(row = 2, column = 1)

main_window.mainloop()