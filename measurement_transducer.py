import tkinter as tk

# Functions for measurement conversion
def calculate_mile():
    mile = float(entry_mile.get())
    km = round(mile * 1.60934, 2)
    label_result1['text'] = f"km: {km}"

def calculate_km():
    km = float(entry_km.get())
    mile = round(km * 0.621371, 2)
    label_result2['text'] = f"mile: {mile}"

def calculate_kg():
    kg = float(entry_kg.get())
    lbs = round(kg * 2.20462, 2)
    label_result3['text'] = f"lbs: {lbs}"

def calculate_lbs():
    lbs = float(entry_lbs.get())
    kg = round(lbs * 0.453592, 2)
    label_result4['text'] = f"kg: {kg}"

# Create main window
root = tk.Tk()
root.title("Measurement Transducer")
root.geometry("450x300")
root.configure(bg="lightgray")

# Create labels and entry fields
label_mile = tk.Label(root, text="mile:", bg="lightgray")
label_km = tk.Label(root, text="km:", bg="lightgray")
entry_mile = tk.Entry(root)
entry_km = tk.Entry(root)

label_kg = tk.Label(root, text="kg:", bg="lightgray")
label_lbs = tk.Label(root, text="lbs:", bg="lightgray")
entry_kg = tk.Entry(root)
entry_lbs = tk.Entry(root)

# Create buttons for conversions
button_calculate_mile = tk.Button(root, text="Convert mi to km", command=calculate_mile)
button_calculate_km = tk.Button(root, text="Convert km to mi", command=calculate_km)
button_calculate_kg = tk.Button(root, text="Convert kg to lbs", command=calculate_kg)
button_calculate_lbs = tk.Button(root, text="Convert lbs to kg", command=calculate_lbs)

# Create result labels
label_result1 = tk.Label(root, text="km:", bg="lightgray")
label_result2 = tk.Label(root, text="mile:", bg="lightgray")
label_result3 = tk.Label(root, text="lbs:", bg="lightgray")
label_result4 = tk.Label(root, text="kg:", bg="lightgray")

# Organize widgets using grid layout
label_mile.grid(row=0, column=0, padx=10, pady=5)
entry_mile.grid(row=0, column=1, padx=10, pady=5)
label_km.grid(row=1, column=0, padx=10, pady=5)
entry_km.grid(row=1, column=1, padx=10, pady=5)
label_kg.grid(row=6, column=0, padx=10, pady=5)
entry_kg.grid(row=6, column=1, padx=10, pady=5)
label_lbs.grid(row=7, column=0, padx=10, pady=5)
entry_lbs.grid(row=7, column=1, padx=10, pady=5)

button_calculate_mile.grid(row=2, column=0, padx=10, pady=5)
button_calculate_km.grid(row=3, column=0, padx=10, pady=5)
button_calculate_kg.grid(row=8, column=0, padx=10, pady=5)
button_calculate_lbs.grid(row=9, column=0, padx=10, pady=5)

label_result1.grid(row=2, column=1, padx=10, pady=5)
label_result2.grid(row=2, column=2, padx=10, pady=5)
label_result3.grid(row=8, column=1, padx=10, pady=5)
label_result4.grid(row=8, column=2, padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
