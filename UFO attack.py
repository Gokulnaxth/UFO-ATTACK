import turtle
import random
import math
score = 0

sc=turtle.Screen()# to create the screen
sc.title("UFO Attack")
sc.bgcolor("Black")
sc.setup(600,600)
sc.tracer(0)

sc.register_shape("PLAY.gif")
sc.register_shape("gok.gif")

player = turtle.Turtle()# code for the player
player.shape("PLAY.gif")
player.penup()
player.goto(0,-275)

enemies=[]#code for the enemy
no_enemy= 5

for i in range(no_enemy):
    x=random.randint(-265,265)
    y=random.randint(100,250)
    enemy = turtle.Turtle()
    enemy.shape("gok.gif")
    enemy.penup()
    enemy.goto(x,y)
    enemies.append(enemy)

enemyspeed= 0.02

bul = turtle.Turtle()#code for the bullet
bul.shape("triangle")
bul.color("Yellow")
bul.shapesize(0.5)
bul.penup()
bul.goto(0,-265)
bul.setheading(90)
bulspeed = 0.3
bulstate="ready"
bul.hideturtle()

pen = turtle.Turtle()#code for the score
pen.color("white")
pen.penup()
pen.goto(0,265)
pen.write("Score:0", align = "center",font= ("arial",22,"bold"))
pen.hideturtle()

def player_left():# player to left
    x = player.xcor()
    x-=20
    if x<-270:
        x= -270
    player.setx(x)

def player_right():# player to right
    x = player.xcor()
    x+=20
    if x>270:
        x=270
    player.setx(x)

def fire_bullet():
    global bulstate
    if bulstate == "ready":
        bulstate="fire"
        bul.showturtle()
        x=player.xcor()
        y=player.ycor() + 10
        bul.goto(x,y)

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
                       
    
sc.listen()# key board binding
sc.onkeypress(player_left,"Left")
sc.onkeypress(player_right,"Right")
sc.onkeypress(fire_bullet,"space")

while True:
    sc.update()

    for enemy in enemies:
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        
        if enemy.xcor()> 270:
            for e in enemies:
                y = e.ycor()
                y-=40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor()< -270:
            for e in enemies:
                y = e.ycor()
                y-= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bul,enemy):
            bul.hideturtle()
            bul.state = "ready"
            bul.goto(0,-400)
            x=random.randint(-265,265)
            y=random.randint(100,250)
            enemy.goto(x,y)
            score += 1
            pen.clear()
            pen.write("Score:{}".format(score), align = "center",font= ("arial",22,"bold"))

        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("GAME OVER")
            exit()
            
            

    if bulstate == "fire":
        y=bul.ycor()
        y+= bulspeed
        bul.sety(y)

    if bul.ycor() > 250:
        bul.hideturtle()
        bulstate = "ready"



    
            

        
        

        

