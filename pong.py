import turtle
import winsound
  
wn = turtle.Screen()
wn.title("Pong by AYES")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)   
wn.tracer(0)

#score
score_enes = 0
score_aysu = 0

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle b
paddle_b= turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid = 5,stretch_len = 1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("ENES: 0 AYSU: 0", align="center",font=("Courier", 24, "normal"))

#function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 50
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 50
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 50
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 50
    paddle_b.sety(y)


#keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") 
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up") 
wn.onkeypress(paddle_b_down,"Down")


#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_enes += 1
        pen.clear()
        winsound.PlaySound("losing.wav",winsound.SND_ASYNC)
        pen.write("ENES: {} AYSU: {}".format(score_enes,score_aysu), align="center",font=("Courier", 24, "normal")) 

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_aysu += 1
        pen.clear()
        winsound.PlaySound("losing.wav",winsound.SND_ASYNC)
        pen.write("ENES: {} AYSU: {}".format(score_enes,score_aysu), align="center",font=("Courier", 24, "normal"))      

    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)   
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC) 
