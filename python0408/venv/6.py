import turtle
t=turtle.Turtle()
t.shape("turtle")

color_list=["yellow","red","blue","green","pink","brown","skyblue"]


for i in range(0,7,1):
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    t.forward(30)

turtle.exitonclick()