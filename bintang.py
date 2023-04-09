import turtle

ukuran = int(input('Masukan ukuran bintang: '))
star = turtle.Turtle()
for i in range (5):
    star.forward(ukuran)
    star.right(144)
turtle.done()