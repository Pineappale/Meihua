import turtle
import random
from turtle import *
from time import sleep

t = turtle.Turtle()#绘图区域
w = turtle.Screen() #画布大小


def tree(branchLen,t):#画梅花的躯干
    if branchLen>3:
        if 8<=branchLen<=12:#躯干数大于8到12进行随机落花瓣
            if random.randint(0,2)==0:
                t.color('snow')#花瓣
            else:
                t.color('lightcoral')
            t.pensize(branchLen/3)
        elif branchLen<8:
            if random.randint(0,1)==0:
                t.color('snow')
            else:
                t.color('lightcoral')
            t.pensize(branchLen/2)
        else:
            t.color('sienna')
            t.pensize(branchLen/10)
        t.forward(branchLen)
        a=1.5*random.random()
        t.right(20*a)
        b=1.5*random.random()
        tree(branchLen-10*b,t)
        t.left(40*a)
        tree(branchLen - 10*b, t)
        t.right(20*a)
        t.up()
        t.backward(branchLen)
        t.down()


def petal(m,t):#掉落的花瓣
    for i in range(m):
        a=200-400*random.random()
        b =10-20*random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        t.color('lightcoral')
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)


def main():#绘制梅花
    t=turtle.Turtle()
    myWin=turtle.Screen()
    Screen().tracer(5,0)
    turtle.screensize(bg='wheat')
    t.left(90)
    t.up()
    t.backward(150)
    t.down()
    t.color('sienna')
    tree(60,t)
    petal(100,t)

    myWin.exitonclick()


main()
