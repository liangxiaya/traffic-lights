import turtle
import time
t=turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
color=["white","white","red","white","yellow","white","white","white","green"]
t.penup()
t.goto(-185,-100)
t.pendown()
t.color("white")
t.write("作者：电脑x",font=("宋体",50,"normal"))
t.penup()
t.goto(-100,150)
t.pendown()
t.write("红绿灯",font=("宋体",50,"normal"))
t.penup()
t.goto(-235,-150)
t.pendown()
t.write("哔哩哔哩 (゜-゜)つロ 干杯~-bilibili",font=("宋体",20,"normal"))
t.pensize(5)
y = 0
作者电脑x = 0
while 作者电脑x == 0:
    if y==0:
        d=1
        n=-2
        x=-1
    else:
        d=-1
        n=2
        x=1
    for i in range(d,n,x):
        t.penup()
        t.goto(i*150,0)
        t.pendown()
        t.color("white",color[y])
        t.begin_fill()
        t.circle(50)
        t.end_fill()
        if y ==8:
            y = 0
        else:
            y = y + 1
    time.sleep(1)