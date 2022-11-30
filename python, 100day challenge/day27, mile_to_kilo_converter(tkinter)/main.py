# 해당 모듈을 많이 사용하지않는다면 단순 import문이 좋지만
import tkinter
# 많이 사용한다면 아래 코드와같이 전체 호출뒤 사용하는게 좋다.
from tkinter import *

window = Tk()
window.title("Challenge")
window.minsize(width=150, height=80)
window.config(padx=20, pady=20)

is_label = Label(text="is equal to")
is_label.grid(column=0, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
result_label = Label(text="0")
result_label.grid(column=1, row=1)

def mile_to_km():
    result = int(entry.get()) * 1.609
    result_label.config(text=result)

calculate_button = Button(text="Calculate", command=mile_to_km)
calculate_button.grid(column=1, row=2)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)



window.mainloop()