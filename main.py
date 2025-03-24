import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        Eng = int(eng_entry.get())
        Math = int(math_entry.get())
        Sci = int(sci_entry.get())
        Com = int(com_entry.get())
        Phy = int(phy_entry.get())

        Average = (Eng + Math + Sci + Com + Phy) / 5

        if Average > 85:
            grade_label.config(text="Grade A")
        elif Average > 70 and Average <= 80:
            grade_label.config(text="Grade B")
        elif Average > 60 and Average <= 70:
            grade_label.config(text="Grade C")
        elif Average > 45 and Average <= 60:
            grade_label.config(text="Grade D")
        else:
            grade_label.config(text="Grade E")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for all subjects")

# Create the main window
root = tk.Tk()
root.title("Grade Calculator")
root.geometry("400x300") # Set the window size to 400x300

# Create input labels and entry fields
label_font = ("Helvetica", 30)
entry_font = ("Helvetica", 30)
eng_label = tk.Label(root, text="English:")
eng_label.pack()
eng_entry = tk.Entry(root)
eng_entry.pack()

math_label = tk.Label(root, text="Maths:")
math_label.pack()
math_entry = tk.Entry(root)
math_entry.pack()

sci_label = tk.Label(root, text="Science:")
sci_label.pack()
sci_entry = tk.Entry(root)
sci_entry.pack()

com_label = tk.Label(root, text="Computer:")
com_label.pack()
com_entry = tk.Entry(root)
com_entry.pack()

phy_label = tk.Label(root, text="Physics:")
phy_label.pack()
phy_entry = tk.Entry(root)
phy_entry.pack()

calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.pack()

grade_label = tk.Label(root, text="")
grade_label.pack()

# Start the GUI main loop
root.mainloop()
