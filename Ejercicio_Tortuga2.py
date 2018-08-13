import turtle



fwd = input("digte el tamaño: ")

window = turtle.Screen()

def dibujo(fwd):
    x = 1
    square = turtle.Turtle()
    while x <= 4:
        square.forward(fwd)
        square.left(90)
        x = x+1
    turtle.mainloop()

dibujo(int(fwd))