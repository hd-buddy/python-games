# Dhruv Hingu (aka BUDDY..)
# Created with help of youtube video link is given below:
# https://www.youtube.com/watch?v=XGf2GcyHPhc


import turtle
import winsound
wn=turtle.Screen()
wn.title("My First Game -- Dhruv Hingu")
wn.bgcolor("yellow")
wn.setup(width=800,height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_len=1,stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_len=1,stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4

# Intializing Score
score_a=0
score_b=0

# Stats
pen=turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A : {}  Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))

# Moving Paddles
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)
    
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)    

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)
    
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)
    
def paddle_a_up_fast():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)   
     
# Keyboard Binding 
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(paddle_a_up_fast,"W")

while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    # Border Checking Upper nd Lower
    if (ball.ycor()>290):
        ball.sety(290)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dy *= -1
        
    if (ball.ycor()<-290):
        ball.sety(-290)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dy *= -1
        
    # Testing part for Left nd Right
    if (ball.xcor()>390):
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    if (ball.xcor()<-390):
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A : {}  Player B : {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
    
    if (score_a>=5 or score_b>=5):
        wn.clear()
        wn.bgcolor("yellow")
        paddle_a.hideturtle()
        paddle_b.hideturtle()
        ball.hideturtle()
        pen2=turtle.Turtle()
        pen2.speed(0)
        pen2.color("Black")
        pen2.penup()
        pen2.hideturtle()
        pen2.goto(0,0)
        if(score_a==5):
            pen2.write("Player A wins!!!",align="center",font=("Elephant",60,"normal"))
            pen2.goto(-50,0)
            pen2.write("Click Here to Exit....",align="center",font=("Times New Roman",10,"normal"))
            wn.listen()
            wn.exitonclick()
        else:
            pen2.write("Player B wins!!!",align="center",font=("Elephant",60,"normal"))
            pen2.goto(-50,0)
            pen2.write("Click Here to Exit....",align="center",font=("Times New Roman",10,"normal"))
            wn.listen()
            wn.exitonclick()
        break
        
    # Paddle nd Ball collisions

    # Moving Paddle A
    if ((ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() >paddle_a.ycor()-50)):
        ball.setx(-340)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dx*=-1    
        
    # Moving Paddle B    
    if ((ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() >paddle_b.ycor()-50)):
        ball.setx(340)
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        ball.dx*=-1    
           




