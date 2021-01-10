from tkinter import *

window = Tk()
window.title("Miles To KMS Converter")
window.minsize(width=400, height=400)
window.config(padx=140, pady=140)

label_miles = Label(text="Miles", font=("Arial", 18))
label_miles.grid(row=0, column=1)

label_is_equal_to = Label(text="Is  equal to", font=("Arial", 16))
label_is_equal_to.grid(row=2, column=0)

label_kms = Label(text="Kms", font=("Arial", 18))
label_kms.grid(row=2, column=2)


def miles_to_kms(x):
    return x * 1.60934


miles = Entry(width=20)
miles.insert(END, string="0")
miles.grid(row=0, column=0)

kms = Entry(width=20)
kms.grid(row=2, column=1)


def button_clicked():
    kms.delete(0, 'end')
    input_miles = miles.get()
    km = miles_to_kms(int(input_miles))
    kms.insert(END, string=f"{km}")


my_button = Button(text="Calculate", command=button_clicked)
my_button.grid(row=3, column=1)

window.mainloop()
