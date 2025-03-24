from tkinter import*

main_window = Tk()

# Labels
Label(main_window, text="What's your name").grid(row = 0, column = 0)
Label(main_window, text= "What's your age").grid(row = 1, column = 0)

# Text Input
Name = Entry(main_window, width= 50, borderwidth= 5).grid(row = 0, column = 1)
Age = Entry(main_window, width= 50, borderwidth= 5).grid(row = 1, column = 1)

def on_click():
    print(f"my name is {Name}, and my age is {Age}")

# Button
Button(main_window, text= "Click Me", command = on_click).grid(row = 2, column = 1)

main_window.mainloop()