import turtle

t=turtle.Turtle()

s=turtle.textinput('즐거운 씨큐브 코딩','이름을 알려주세요')
t.write("%s님 반갑습니다^^" % s)

t=turtle.Turtle(shape="turtle")

n=turtle.numinput(s,"앞으로 얼마나 이동할까요?")
t.forward(n)

ang=turtle.numinput(s,"오른쪽으로 얼마나 회전할까요?:", default=0, minval=0, maxval=3600)
t.right(ang)

turtle.done()
