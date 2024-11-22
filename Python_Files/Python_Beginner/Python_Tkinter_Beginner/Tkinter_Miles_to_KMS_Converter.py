from tkinter import *

window = Tk()

window.title("Convert Miles to Kilometers")

window.minsize(width=400,height=200)
window.maxsize(width=400,height=200)
window.config(padx=20,pady=20)
window.config(bg="black")

def miles_to_kms():
    miles = float(miles_input.get())
    kms = round(miles * 1.609,2)
    km_result_label.config(text = kms)


miles_input = Entry(width=7,bg="black",fg="white")
miles_input.grid(column=1,row=0)

miles_label = Label(text="Miles",bg="black",fg="white")
miles_label.grid(column=2,row=0)

is_equal = Label(text="is equal to",bg="black",fg="white")
is_equal.grid(column=0,row=1)

km_result_label = Label(text="0",bg="black",fg="white")
km_result_label.grid(column=1,row=1)


Km_label = Label(text="kms",bg="black",fg="white")
Km_label.grid(column=2,row=1) 


calculate_button = Button(text="Calculate",bg="black",fg="white",command=miles_to_kms)
calculate_button.grid(column=1,row=2)








window.mainloop()