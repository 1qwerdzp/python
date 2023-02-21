import turtle

t=turtle.Turtle()

t.penup()
t.goto(150,0)
t.pendown()
t.color("#000000")
t.fillcolor("#00AAFF")

t.begin_fill()
t.goto(200,0)
t.goto(200,50)
t.goto(150,50)
t.end_fill()

t.fillcolor("#00FFFF")

t.begin_fill()
t.goto(175,100)
t.goto(200,50)
t.goto(150,50)
t.goto(150,0)
t.end_fill()

t.goto(-200,0)

a=1

w=["apple","python","game","turtle","color"]

T=turtle.textinput("fruit",str(w)+str(a)+"/6")


turtle.done()