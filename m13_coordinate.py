from tkinter import Tk, Canvas

window = Tk()
window.geometry("400x300")
canvas = Canvas(window, width=400, height=300)
canvas.pack()

x_center = 200
y_center = 150
radius = 50
canvas.create_oval(x_center - radius, y_center - radius, x_center + radius, y_center + radius, fill="blue")

canvas.create_rectangle(210, 210, 280, 280, fill="yellow")

window.mainloop()