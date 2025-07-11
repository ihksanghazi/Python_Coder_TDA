from tkinter import Tk, Entry, Label, Button

root = Tk()
root.title("Tkinter Example")

root.geometry("400x100")

label = Label(root, text="Enter Your Name:")
label.pack()

entry = Entry(root)
entry.pack()

button = Button(root, text="Greet Me")
button.pack()

root.mainloop()