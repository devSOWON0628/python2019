import turtle

t=turtle.Turtle()
t.up()
t.goto(-100,-100)
t.down()
t.shape("turtle")
#n=int(input("몇각형을 그리시겠어요?(3-12):"))
n=int(turtle.textinput("","몇각형을 그리시겠어요(3-6)"))

for i in range(n):
    t.forward(100)
    t.left(360//n)

x=7
y=3
print(x+y)

x='7'
y='3'
print(x+y)



turtle.exitonclick()