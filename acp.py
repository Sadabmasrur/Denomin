import tkinter as tk
from datetime import date

def calculate_age():
    try:
        d = int(day.get())
        m = int(month.get())
        y = int(year.get())
        b = date(y, m, d)
        t = date.today()
        a = t.year - b.year - ((t.month, t.day) < (b.month, b.day))
        result.config(text=f"Age: {a}")
    except:
        result.config(text="Invalid input")

root = tk.Tk()
root.title("Age Calculator")

tk.Label(root, text="Day").pack()
day = tk.Entry(root)
day.pack()

tk.Label(root, text="Month").pack()
month = tk.Entry(root)
month.pack()

tk.Label(root, text="Year").pack()
year = tk.Entry(root)
year.pack()

tk.Button(root, text="Calculate", command=calculate_age).pack()
result = tk.Label(root, text="Age:")
result.pack()

root.mainloop()
