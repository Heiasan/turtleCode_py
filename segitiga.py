import turtle

ukuran = int(input('Masukan ukuran sisi ? '))
a = turtle.Turtle()
for i in range(3):
    a.forward(ukuran)
    a.left(120)
turtle.done()