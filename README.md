
import tkinter as tk
from tkinter import messagebox
def main(name, age, weight, height, bp, pulserate, rbccount, wbccount, platelets, hb, 
uricacid, cholestrol):

 """Generates a fitness report."""
 
 bmi = weight / (height ** 2)
 bmi_label = "High" if bmi > 25 else "Medium" if bmi > 18 else "Low"
 bp_label = "High" if bp > 120 else "Medium" if bp > 90 else "Low"
 pulserate_label = "High" if pulserate > 100 else "Medium" if pulserate > 60 else "Low"
 rbccount_label = "High" if rbccount > 610000 else "Medium" if rbccount > 475000 else 
"Low"
 wbccount_label = "High" if wbccount > 10000 else "Medium" if wbccount > 4000 else 
"Low"
 platelets_label = "High" if platelets > 450000 else "Medium" if platelets > 150000 else 
"Low"
 hb_label = "High" if hb > 16 else "Medium" if hb > 12 else "Low"
 uricacid_label = "High" if uricacid > 7 else "Medium" if uricacid > 4 else "Low"
 cholestrol_label = "High" if cholestrol > 50 else "Medium" if cholestrol > 40 else "Low"
 report = f"""
 
Fitness Report for {name}
Age: {age}
Weight: {weight} kg
Height: {height} m
BMI: {bmi:.2f} ({bmi_label})
BP: {bp} ({bp_label})

Pulse Rate: {pulserate} ({pulserate_label})
RBC Count: {rbccount} ({rbccount_label})
WBC Count: {wbccount} ({wbccount_label})
Platelets: {platelets} ({platelets_label})
Hemoglobin: {hb} ({hb_label})
Uric Acid: {uricacid} ({uricacid_label})
Cholesterol: {cholestrol} ({cholestrol_label})
Overall Fitness: {max(bmi_label, bp_label, pulserate_label, rbccount_label, wbccount_label, 
platelets_label, hb_label, uricacid_label, cholestrol_label)}
"""
 tk.messagebox.showinfo("Fitness Report", report)
def clear_textbox():
 """Clears all the textboxes."""
 for entry in [E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E50, E51]:
 entry.delete(0, tk.END)
def close_window():
 """Closes the window."""
 top.destroy()
top = tk.Tk()
top.title("Fitness Calculator")
# Create the labels and entries
L1 = tk.Label(top, text="Name:")
L1.grid(row=0, column=0)
E1 = tk.Entry(top)
E1.grid(row=0, column=1)

L2 = tk.Label(top, text="Age:")
L2.grid(row=1, column=0)
E2 = tk.Entry(top)
E2.grid(row=1, column=1)

L3 = tk.Label(top, text="Weight (kg):")
L3.grid(row=2, column=0)
L3 = tk.Label(top, text="Weight (kg):")
L3.grid(row=2, column=0)
E3 = tk.Entry(top)
E3.grid(row=2, column=1)
L4 = tk.Label(top, text="Height (m):")
L4.grid(row=3, column=0)
E4 = tk.Entry(top)
E4.grid(row=3, column=1)
L5 = tk.Label(top, text="BP (0-120):")
L5.grid(row=4, column=0)
E5 = tk.Entry(top)
E5.grid(row=4, column=1)
L6 = tk.Label(top, text="Pulse Rate (0-100):")
L6.grid(row=5, column=0)

E6 = tk.Entry(top)
E6.grid(row=5, column=1)
L7 = tk.Label(top, text="RBC Count (310000-610000):")
L7.grid(row=6, column=0)
E7 = tk.Entry(top)
E7.grid(row=6, column=1)
L8 = tk.Label(top, text="WBC Count (2000-10000):")
L8.grid(row=7, column=0)
E8 = tk.Entry(top)
E8.grid(row=7, column=1)
L9 = tk.Label(top, text="Platelets (150000-615000):")
L9.grid(row=8, column=0)
E9 = tk.Entry(top)
E9.grid(row=8, column=1)
L10 = tk.Label(top, text="Hemoglobin (0-16):")
L10.grid(row=9, column=0)
E10 = tk.Entry(top)
E10.grid(row=9, column=1)
L50 = tk.Label(top, text="Uric Acid (0-7):")
L50.grid(row=10, column=0)
E50 = tk.Entry(top)

E50.grid(row=10, column=1)
L51 = tk.Label(top, text="Cholesterol (40-55):")
L51.grid(row=11, column=0)
E51 = tk.Entry(top)
E51.grid(row=11, column=1)


# Create the buttons
B1 = tk.Button(top, text="Generate Report", command=lambda: main(E1.get(), 
int(E2.get()), int(E3.get()), float(E4.get()), int(E5.get()), int(E6.get()), int(E7.get()), 
int(E8.get()), int(E9.get()), int(E10.get()), int(E50.get()), int(E51.get())))
B1.grid(row=12, column=1)
B2 = tk.Button(top, text="Reset All Entries", command=clear_textbox)
B2.grid(row=13, column=1)
B3 = tk.Button(top, text="Exit", command=close_window)
B3.grid(row=14, column=1)
D = tk.Label(top, text="Developed by: Aryan Dangwal and Tanay Gupta", font=("Arial", 
10, "bold"))
D.grid(row=15, column=1)

# Create a root window
root = tk.Tk()

# Display a message box
messagebox.showinfo("Title", "This is the message box.")
# Start the mainloop
root.mainloop()
top.mainloop()
