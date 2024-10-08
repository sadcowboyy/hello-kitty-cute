import turtle

t = turtle.Turtle()
tela = turtle.Screen()
tela.setup(200, 200)
tela.bgcolor('lightpink')
t.color('white')
t.speed(4)
t.pensize(10)
t.begin_fill()
t.circle(150, 360 / 4 + 40)
t.left(30)
t.circle(60, 360 / 4)
t.setheading(170)
t.circle(288, 16)

t.color('white')
t.up()
t.goto(2, 0)
t.setheading(180)
t.down()
t.circle(-150, 360 / 4 + 40)
t.right(30)
t.circle(-58, 360 / 4)
t.end_fill()
t.pensize(2)
# medidas (300px media)
# t.left(180)
# t.fd(150)
# t.back(300)
# t.up()
# t.back  (100)
# t.down()
# t.setheading(90)
# t.fd(300)


# olhos
t.up()
t.goto(80, 130)
t.color('black')
t.down()
t.begin_fill()
t.circle(10, 360)
t.end_fill()

t.up()
t.goto(-80, 130)
t.color('black')
t.down()
t.begin_fill()
t.circle(10, 360)
t.end_fill()
t.up()
t.home()

# nariz

t.up()
t.goto(-5, 80)
t.color('yellow')
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()

t.color('black')
t.pensize(3)
t.circle(10)

# bigodinhos:

# 1
t.up()
t.goto(130, 130)
t.pensize(10)
t.down()
t.circle(50, 9)
t.circle(-100, 20)

# 2
t.up()
t.goto(140, 100)
t.down()
t.circle(50, 9)
t.circle(-90, 10)
t.circle(-60, 11)

# 3
t.up()
t.goto(110, 75)
t.down()
t.circle(50, 9)
t.circle(-125, 10)

# 4
t.up()
t.goto(-130, 130)
t.pensize(10)
t.left(190)
t.down()
t.circle(50, 9)
t.circle(100, 20)

# 5
t.up()
t.goto(-140, 100)
t.down()
t.circle(50, 9)
t.circle(90, 9)

# 6
t.up()
t.goto(-110, 75)
t.down()
t.circle(150, 15)

# levando até a orelha direita
t.up()
t.home()
t.goto(60, 205)

# orelha direita
t.color('pink')
t.down()
t.begin_fill()
t.left(70)
t.circle(-70, 30)
t.circle(-10, 30)
t.circle(-30, 105)
t.right(75)
t.circle(-165, 18)
t.end_fill()

# levando até a orelha esquerda
t.up()
t.home()
t.goto(-60, 205)
t.setheading(111)

# orelha esquerda
t.color('pink')

t.down()
t.begin_fill()
t.circle(70, 30)
t.circle(10, 30)
t.circle(30, 105)
t.right(-75)
t.circle(165, 18)
t.end_fill()

tela.exitonclick()