import turtle
import random
import time
import os

author = 'Author: Homyak'

#Settings
balance = 10000

directory = os.getcwd()

def auth():
    global author
    aut.up()
    aut.goto(220,-250)
    aut.write(author, font=("Arial", 20, "normal"))

def close():
    ex.penup()
    ex.goto(-350, 250)
    ex.write('Press X to close', font=("Arial", 20, "normal"))

def casino():
    global balance
    global bet
    one = random.randint(0,9)
    two = random.randint(0,9)
    three = random.randint(0,9)
    slt.penup()
    slt.goto(-155,-50)
    slt.write(f'{one}   {two}   {three}', font=("Arial", 90, "normal"))
    if one == two == three:
        slt.goto(-80,140)
        slt.write('You won!', font=("Arial", 30, "normal"))
        balance += bet * 100
        mon.clear()
        money(balance)
    else:
        slt.goto(-80,140)
        slt.write('You lose', font=("Arial", 30, "normal"))

def btnclick(x, y):
    global balance
    global bet
    """Клик по кнопке"""
    px, py = btn.pos()
    bx, by = bt.pos()

    if px<x<px+50 and py<y<py+150:
        if balance >= bet:
            slt.clear()
            balance -= bet
            mon.clear()
            money(balance)
            casino()
        else:
            pass
    elif bx<x<bx+150 and by<y<by+50:
        if bet < 1000:
            bet += 50
        else:
            bet = 50
        betting()
           
def draw_bth():
    """Кнопка с надписью"""
    btn.speed(0)
    btn.penup()
    btn.setpos(-100, -200)
    btn.pendown()
    btn.color('black','red')
    btn.begin_fill()
    
    for i in range(4):
        if i in [1,3]:
            btn.fd(50)
        else:
            btn.fd(150)
        btn.left(90)
    
    btn.end_fill()
    btn.penup()
    
    btn.sety(btn.ycor() + 10)
    btn.setx(btn.xcor() + 50)
    
    btn.write('Spin', font=("Arial", 20, "normal"))

def money(balance):
    mon.penup()
    mon.goto(-350,-250)
    mon.write(f'Your balance: {balance}', font=("Arial", 20, "normal"))

def betting():
    global bet
    bt.clear()
    bt.penup()
    bt.setpos(100, -200)
    bt.pendown()
    bt.color('black')
    for i in range(4):
        if i in [1,3]:
            bt.fd(50)
        else:
            bt.fd(150)
        bt.left(90)
    bt.penup()
    bt.sety(bt.ycor() + 50/2 - 12)
    bt.setx(bt.xcor() + 40)
    bt.write(f'Bet: {bet}', font=("Arial", 20, "normal"))
      
screen = turtle.Screen()
screen.setup(1000, 600)
screen.bgpic(f'{directory}/casino.gif')

aut =  turtle.Turtle()
aut.hideturtle()
aut.speed(0)

slt =  turtle.Turtle()
slt.hideturtle()
slt.speed(0)

ex = turtle.Turtle()
ex.hideturtle()
ex.speed(0)

mon = turtle.Turtle()
mon.hideturtle()
mon.speed(0)

bt = turtle.Turtle()
bt.hideturtle()
bt.speed(0)

btn = turtle.Turtle()
btn.speed(0)
btn.hideturtle()

bet = 50

if __name__ == '__main__':
    auth()
    close()
    draw_bth()
    money(balance)
    betting()

    time.sleep(1)
    screen.listen()
    screen.onscreenclick(btnclick, 1)

    screen.onkeypress(lambda: turtle.bye(), 'x')
    turtle.mainloop()