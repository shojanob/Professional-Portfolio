from tkinter import *


def button_clicked():
    print("I got clicked")
    word = input.get()
    my_label.config(text=word)

window = Tk()
window.title("Shoh's First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=100,y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button_2 = Button(text="Touch Me", command=button_clicked)
button_2.grid(column=2,row=0)

# Entry
input = Entry(width=10)
print(input.get())
# input.pack()
input.grid(column=3,row=2)


window.mainloop()