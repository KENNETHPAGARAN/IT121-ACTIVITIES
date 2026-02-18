import tkinter as tk
from tkinter import messagebox

def calculate_grade():
    try:
        number = entry_number.get()
        name = entry_name.get()
        course = entry_course.get()
        prelim = float(entry_prelim.get())
        midterm = float(entry_midterm.get())
        final = float(entry_final.get())

        average = (prelim * 0.20) + (midterm * 0.30) + (final * 0.50)

        if average >= 75:
            remarks = "Passed"
        else:
            remarks = "Failed"

        result_text.set(
            f"Student Number: {number}\n"
            f"Student Name: {name}\n"
            f"Course: {course}\n"
            f"Average: {round(average,2)}\n"
            f"Remarks: {remarks}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for grades!")

def clear_fields():
    entry_number.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_prelim.delete(0, tk.END)
    entry_midterm.delete(0, tk.END)
    entry_final.delete(0, tk.END)
    result_text.set("")

window = tk.Tk()
window.title("Grade Calculator")
window.geometry("400x500")

tk.Label(window, text="Student Number").pack()
entry_number = tk.Entry(window)
entry_number.pack()

tk.Label(window, text="Student Name").pack()
entry_name = tk.Entry(window)
entry_name.pack()

tk.Label(window, text="Course").pack()
entry_course = tk.Entry(window)
entry_course.pack()

tk.Label(window, text="Prelim Grade").pack()
entry_prelim = tk.Entry(window)
entry_prelim.pack()

tk.Label(window, text="Midterm Grade").pack()
entry_midterm = tk.Entry(window)
entry_midterm.pack()

tk.Label(window, text="Final Grade").pack()
entry_final = tk.Entry(window)
entry_final.pack()

tk.Button(window, text="Calculate", command=calculate_grade).pack(pady=10)
tk.Button(window, text="Clear", command=clear_fields).pack()

result_text = tk.StringVar()
tk.Label(window, textvariable=result_text, justify="left").pack(pady=20)

window.mainloop()
