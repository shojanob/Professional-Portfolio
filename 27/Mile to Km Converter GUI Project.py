from tkinter import *

def calculate_km():
    miles = miles_input.get()
    convert_to_km = float(miles) * 1.609
    km_output.config(text=convert_to_km)

window = Tk()
window.title("Shoh's Mile to Km Converter")
window.minsize(height=300, width=300)

# Labels
miles_label = Label(text="Miles", font=("Arial", 11, "normal"))
miles_label.grid(column=2,row=0)
miles_label.config(pady=10, padx=10)

is_equal_to_label = Label(text="is equal to", font=("Arial", 11, "normal"))
is_equal_to_label.grid(column=0,row=1)

km_label = Label(text="Km", font=("Arial", 11, "normal"))
km_label.grid(column=2,row=1)

km_output = Label(text="0", font=("Arial", 11, "normal"))
km_output.grid(column=1, row=1)

# Entry
miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

# Button
calculate_button = Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1,row=2)



window.mainloop()