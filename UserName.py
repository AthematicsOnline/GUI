import tkinter as tk
from tkinter import ttk, filedialog

def submit():
    name = name_entry.get()
    gender = gender_var.get()
    age = age_spinbox.get()
    password = password_entry.get()
    comment = comment_text.get("1.0", "end-1c")

    print("Name:", name)
    print("Gender:", gender)
    print("Age:", age)
    print("Password:", password)
    print("Comment:", comment)
    print("Passport:", passport_path.get())  # Added to display selected passport path

def browse_passport():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")])
    passport_path.set(file_path)

# Create the main window
root = tk.Tk()
root.title("Simple GUI Example")

# Create and place labels and input fields using grid
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=1, column=0, sticky=tk.W)
gender_var = tk.StringVar(value="Male")  # Default value
gender_radios = ttk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
gender_radios.grid(row=1, column=1, sticky=tk.W)
gender_radios = ttk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
gender_radios.grid(row=1, column=2, sticky=tk.W)

age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, sticky=tk.W)
age_spinbox = tk.Spinbox(root, from_=1, to=120)
age_spinbox.grid(row=2, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0, sticky=tk.W)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

comment_label = tk.Label(root, text="Comment:")
comment_label.grid(row=4, column=0, sticky=tk.W)
comment_text = tk.Text(root, height=5)
comment_text.grid(row=4, column=1)

passport_label = tk.Label(root, text="Upload Passport:")
passport_label.grid(row=5, column=0, sticky=tk.W)
passport_path = tk.StringVar()  # To store the selected passport path
passport_entry = tk.Entry(root, textvariable=passport_path, state='disabled')
passport_entry.grid(row=5, column=1)
browse_button = tk.Button(root, text="Browse", command=browse_passport)
browse_button.grid(row=5, column=2)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=6, columnspan=2)

# Start the GUI event loop
root.mainloop()
