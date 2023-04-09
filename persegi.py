import turtle

ukuran = int(input('Panjang sisi ?'))
a = turtle.Turtle()
for i in range(4):
    a.right(90)
    a.forward(ukuran)
turtle.done()