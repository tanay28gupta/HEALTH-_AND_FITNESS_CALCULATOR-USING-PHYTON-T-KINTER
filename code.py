import tkinter as tk
from tkinter import messagebox

def main(name, age, weight, height, bp, pulserate, rbccount, wbccount, platelets, hb, uricacid, cholestrol):
    """Generates a fitness report."""
    bmi = weight / (height ** 2)
    bmi_label = "High" if bmi > 25 else "Medium" if bmi > 18 else "Low"
    bp_label = "High" if bp > 120 else "Medium" if bp > 90 else "Low"
    pulserate_label = "High" if pulserate > 100 else "Medium" if pulserate > 60 else "Low"
    rbccount_label = "High" if rbccount > 610000 else "Medium" if rbccount > 475000 else "Low"
    wbccount_label = "High" if wbccount > 10000 else "Medium" if wbccount > 4000 else "Low"
    platelets_label = "High" if platelets > 450000 else "Medium" if platelets > 150000 else "Low"
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
Overall Fitness: {max(bmi_label, bp_label, pulserate_label, rbccount_label, wbccount_label, platelets_label, hb_label, uricacid_label, cholestrol_label)}
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
labels = ["Name:", "Age:", "Weight (kg):", "Height (m):", "BP (0-120):", "Pulse Rate (0-100):", "RBC Count (310000-610000):", 
          "WBC Count (2000-10000):", "Platelets (150000-615000):", "Hemoglobin (0-16):", "Uric Acid (0-7):", "Cholesterol (40-55):"]

entries = []

for i, label in enumerate(labels):
    tk.Label(top, text=label).grid(row=i, column=0)
    entry = tk.Entry(top)
    entry.grid(row=i, column=1)
    entries.append(entry)

# Create the buttons
tk.Button(top, text="Generate Report", command=lambda: main(*[entry.get() for entry in entries])).grid(row=len(labels), column=1)
tk.Button(top, text="Reset All Entries", command=clear_textbox).grid(row=len(labels) + 1, column=1)
tk.Button(top, text="Exit", command=close_window).grid(row=len(labels) + 2, column=1)

D = tk.Label(top, text="Developed by: Aryan Dangwal and Tanay Gupta", font=("Arial", 10, "bold"))
D.grid(row=len(labels) + 3, column=1)

top.mainloop()

