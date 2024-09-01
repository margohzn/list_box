from tkinter import *

window = Tk()
window.geometry("390x300")

def add():
    listbox.insert(END, entry.get())
    entry.delete(0, END)

widjet_frame = Frame(window)

entry = Entry(widjet_frame, width = 10, font = ("times", 20))
add_button = Button(widjet_frame, text = "Add", font = ("times", 20), width = 7, command = add)
delete_button = Button(widjet_frame, text = "Delete", font = ("times", 20), width = 7)

entry.grid(row = 1, column = 1, ipady = 5, padx = 5)
add_button.grid(row = 1, column = 2, pady = 30, padx = 20, ipady = 5)
delete_button.grid(row = 1, column = 3, ipady = 5, padx = 5)

widjet_frame.grid(row = 1, column = 1)


lisbox_frame = Frame(window)

listbox = Listbox(lisbox_frame, width = 40)
listbox.grid(row = 1, column = 1)

lisbox_frame.grid(row = 2, column = 1)

window.mainloop()