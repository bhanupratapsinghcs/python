import tkinter as tk

root = tk.Tk()

WIDTH = 400
HEIGHT = 400

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)

canvas.pack()

x1 = WIDTH / 2
y1 = HEIGHT / 2

text = canvas.create_text(x1, y1 * 2 - 20, text="Keys to move = a,d,w,s")

image = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)


def move(event):
    global x1, y1
    if event.char == "a":
        canvas.move(image, -10, 0)
    elif event.char == "d":
        canvas.move(image, 10, 0)
    elif event.char == "w":
        canvas.move(image, 0, -10)
    elif event.char == "s":
        canvas.move(image, 0, 10)


root.bind("<Key>", move)


root.mainloop()
