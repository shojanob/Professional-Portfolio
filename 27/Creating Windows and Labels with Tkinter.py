from tkinter import *

window = Tk()
window.title("Shoh's First GUI Program")
window.minsize(width=500, height= 300)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


window.mainloop()