#main.py
import turtle, colorsys, time, random

mywindow = turtle.Screen()
mywindow.title("MISSILE COMMAND: angry arrows")
mywindow.setup(800, 800)

# STARTING SCREEN ---------------------------
mywindow.bgcolor("#1d1e21")

borderboy = turtle.Turtle()
borderboy.hideturtle()
borderboy.penup()
borderboy.shape("square")
borderboy.speed(0)
borderboy.pensize(30)
borderboy.goto(382, 390)
borderboy.pendown()
borderboy.setheading(270)

writerboy = turtle.Turtle()
writerboy.hideturtle()
writerboy.penup()
writerboy.speed(0)

lifeboy = turtle.Turtle()
lifeboy.hideturtle()
lifeboy.penup()
lifeboy.speed(0)
lifeboy.color("#1d1e21")

scoreboy = turtle.Turtle()
scoreboy.hideturtle()
scoreboy.penup()
scoreboy.speed(0)
scoreboy.color("#1d1e21")

levelboy = turtle.Turtle()
levelboy.hideturtle()
levelboy.penup()
levelboy.speed(0)
levelboy.color("white")

hideboy = turtle.Turtle()
hideboy.hideturtle()
hideboy.penup()
hideboy.shape("square")
hideboy.color('#1d1e21')
hideboy.turtlesize(34)
hideboy.goto(0,0)

terrainboy = turtle.Turtle()
terrainboy.hideturtle()
terrainboy.penup()
terrainboy.speed(0)
terrainboy.color("#dbd51a")
terrainboy.pensize(150)
terrainboy.goto(-400, -320)
terrainboy.pendown()

playboy = turtle.Turtle()
playboy.hideturtle()
playboy.penup()
playboy.speed(0)
playboy.color("#3bc427")
playboy.shape("square")
playboy.turtlesize(4, 8)

cursorboy = turtle.Turtle()
cursorboy.hideturtle()
cursorboy.penup()
cursorboy.shape("circle")
cursorboy.pencolor("white")
cursorboy.speed(0)

battery1 = turtle.Turtle()
battery1.hideturtle()
battery1.turtlesize(4)
battery1.penup()
battery1.speed(0)
battery1.color("#dbd51a")
battery1.shape("triangle")
battery1.setheading(90)
b1x = -300
b1y = -225

battery2 = turtle.Turtle()
battery2.hideturtle()
battery2.shape("triangle")
battery2.turtlesize(4)
battery2.penup()
battery2.speed(0)
battery2.color("#dbd51a")
battery2.setheading(90)
b2x = 0
b2y = -225

battery3 = turtle.Turtle()
battery3.hideturtle()
battery3.shape("triangle")
battery3.speed(0)
battery3.turtlesize(4)
battery3.penup()
battery3.setheading(90)
battery3.color("#dbd51a")
b3x = 300
b3y = -225

cities = []
for i in range(0, 6):
  cities.append(turtle.Turtle())
  cities[i].hideturtle()
  cities[i].penup()
  cities[i].speed(0)
  cities[i].color("#1ceaed")
  cities[i].shape("square")
  cities[i].turtlesize(1, 2)

title = ["M", "MI", "MIS", "MISS", "MISSI", "MISSIL", "MISSILE", "MISSILE C", "MISSILE CO", "MISSILE COM",
       "MISSILE COMM", "MISSILE COMMA", "MISSILE COMMAN", "MISSILE COMMAND", ]

b = 0
i = 0
j = 0
while i < 800:
  i += 2.5
  hue = i / 800
  colorTuple = colorsys.hsv_to_rgb(hue, 1, 1)
  borderboy.pencolor(colorTuple)
  if b < 770:
      borderboy.forward(10)
      b += 10
  else:
      b = 0
      borderboy.right(90)
  if j < 14:
      if i > 53 * (j + 1):
          writerboy.clear()
          writerboy.pencolor("white")
          writerboy.write(title[j] + "|", font=("Courier", 40, "bold"), align="center")
          j += 1

writerboy.clear()
writerboy.goto(0,-10)
writerboy.write("Loading...", font=("Courier", 40, "bold"), align="center")
missile1 = []
for i in range(0, 10):
  missile1.append(turtle.Turtle())
  missile1[i].hideturtle()
  missile1[i].penup()
  missile1[i].speed(0)
  missile1[i].color("#09b317")
  missile1[i].turtlesize(1)
  missile1[i].setheading(90)
  missile1[i].pensize(2)

missile2 = []
for i in range(0, 10):
  missile2.append(turtle.Turtle())
  missile2[i].hideturtle()
  missile2[i].penup()
  missile2[i].speed(0)
  missile2[i].color("#09b317")
  missile2[i].turtlesize(1)
  missile2[i].setheading(90)
  missile2[i].pensize(2)

missile3 = []
for i in range(0, 10):
  missile3.append(turtle.Turtle())
  missile3[i].hideturtle()
  missile3[i].penup()
  missile3[i].speed(0)
  missile3[i].color("#09b317")
  missile3[i].turtlesize(1)
  missile3[i].setheading(90)
  missile3[i].pensize(2)

writerboy.speed(4)
writerboy.clear()
writerboy.goto(0, 250)
writerboy.color("white")
writerboy.write("R U L E S", font=("Calibri", 40, "bold", "underline"), align="center")
writerboy.goto(0, 150)
writerboy.write("1) left click to shoot a missile", font=("Calibri", 30, "bold"), align="center")
writerboy.goto(0, 50)
writerboy.write("2) don't let enemy fire hit", font=("Calibri", 27, "bold"), align="center")
writerboy.goto(0, 0)
writerboy.write("your cities or batteries", font=("Calibri", 27, "bold"), align="center")
writerboy.goto(0, -100)
writerboy.write("3) if a battery is lost, replace a city with", font=("Calibri", 23, "bold"), align="center")
writerboy.goto(0, -150)
writerboy.write("a new battery by pressing spacebar", font=("Calibri", 23, "bold"), align="center")
playboy.goto(0, -250)
playboy.stamp()
writerboy.goto(0, -270)
writerboy.write("PLAY", font=("Calibri", 20, "bold"), align="center")

# FUNCTIONS-------------------------------

life = 6
score = 0
level = 1

def set_coords(event):
  global x, y
  x = event.x
  y = event.y

numberofenemy = 2
finish = []
for i in range(0, numberofenemy):
  finish.append(1)

def setup(x,y):
  if -80 <= x <= 80 and -290 <= y <= -210:
      screen.bind('<Motion>', set_coords)
      writerboy.clear()
      playboy.clear()
      playboy.hideturtle()
      levelboy.goto(0, 325)
      levelboy.write("LEVEL " + str(level), font=("Courier", 25, "bold"), align="center")
      scoreboy.goto(-320, -350)
      scoreboy.write("Score: " + str(score), font=("Courier", 15, "bold"), align="left")
      lifeboy.goto(-320, -320)
      lifeboy.write("Lives: " + str(life), font=("Courier", 15, "bold"), align="left")
      terrainboy.goto(400, -320)
      terrainboy.hideturtle()
      battery1.goto(b1x, b1y)
      battery2.goto(b2x, b2y)
      battery3.goto(b3x, b3y)
      battery1.showturtle()
      battery2.showturtle()
      battery3.showturtle()

      for i in range(0, len(cities)):
          cities[i].goto(-220 + (65 * (i)), -235)
          if i > 2:
              cities[i].goto(25 + (65 * (i - 2)), -235)
          cities[i].showturtle()
      for i in range(0, len(missile1)):
          missile1[i].goto(-324 + (15.5 * i), -235)
          if 7 > i > 3:
              missile1[i].goto(-315 + (15 * (i - 4)), -220)
          elif 9 > i > 6:
              missile1[i].goto(-307 + (13.5 * (i - 7)), -205)
          elif i == 9:
              missile1[i].goto(-300, -190)
          missile1[i].showturtle()
          missile1[i].pendown()
          missile1[i].speed(0)
      for i in range(0, len(missile2)):
          missile2[i].goto(-24 + (15.5 * i), -235)
          if 7 > i > 3:
              missile2[i].goto(-15 + (15 * (i - 4)), -220)
          elif 9 > i > 6:
              missile2[i].goto(-7 + (13.5 * (i - 7)), -205)
          elif i == 9:
              missile2[i].goto(0, -190)
          missile2[i].showturtle()
          missile2[i].pendown()
          missile2[i].speed(0)
      for i in range(0, len(missile3)):
          missile3[i].goto(276 + (15.5 * i), -235)
          if 7 > i > 3:
              missile3[i].goto(285 + (15 * (i - 4)), -220)
          elif 9 > i > 6:
              missile3[i].goto(293 + (13.5 * (i - 7)), -205)
          elif i == 9:
              missile3[i].goto(300, -190)
          missile3[i].showturtle()
          missile3[i].pendown()
          missile3[i].speed(0)
      writerboy.color("#1d1e21")
      for i in range(0, 3):
          writerboy.goto(-300 + (300 * i), -265)
          writerboy.write("Battery " + str(i + 1), font=("Courier", 7, "normal"), align="center")
      cursorboy.showturtle()
      spawnenemy()

b1down = False
b2down = False
b3down = False

b1missile = []
b2missile = []
b3missile = []

index1=-1
index2=-1
index3=-1

bullet1finish = []
bullet2finish = []
bullet3finish = []

def click(x,y):
  global index1, index2,index3, b1missile,b2missile,b3missile, bullet1finish, bullet2finish, bullet3finish
  if x <-155 and b1down==False:
      index1 += 1
      b1missile.append([turtle.Turtle(),x,y,False,3])
      b1missile[index1][0].hideturtle()
      b1missile[index1][0].penup()
      b1missile[index1][0].color("#09b317")
      b1missile[index1][0].turtlesize(1)
      b1missile[index1][0].setheading(90)
      b1missile[index1][0].pensize(2)
      b1missile[index1][0].goto(-300, -190)
      b1missile[index1][0].pendown()
      b1missile[index1][0].showturtle()
      bullet1finish.append(1)
  elif -155<=x<=155 and b2down==False:
      index2 += 1
      b2missile.append([turtle.Turtle(),x,y,False,3])
      b2missile[index2][0].hideturtle()
      b2missile[index2][0].penup()
      b2missile[index2][0].color("#09b317")
      b2missile[index2][0].turtlesize(1)
      b2missile[index2][0].setheading(90)
      b2missile[index2][0].pensize(2)
      b2missile[index2][0].goto(0, -190)
      b2missile[index2][0].pendown()
      b2missile[index2][0].showturtle()
      bullet2finish.append(1)
  elif x>155 and b3down==False:
      b3missile.append([turtle.Turtle(),x,y,False,3])
      b3missile[index3][0].hideturtle()
      b3missile[index3][0].penup()
      b3missile[index3][0].color("#09b317")
      b3missile[index3][0].turtlesize(1)
      b3missile[index3][0].setheading(90)
      b3missile[index3][0].pensize(2)
      b3missile[index3][0].goto(300, -190)
      b3missile[index3][0].pendown()
      b3missile[index3][0].showturtle()
      bullet3finish.append(1)
  for z in range(0, len(enemy)):
      enemyfire(enemy[z], assigned[z].xcor(), assigned[z].ycor())

def battery1down():
  global b1down
  battery1.hideturtle()
  battery1.clear()
  b1down = True
  for i in range(0, len(missile1)):
      missile1[i].hideturtle()
      missile1[i].clear()
  for i in range(0, len(b1missile)):
      b1missile[i][0].hideturtle()
      b1missile[i][0].clear()

def battery2down():
  global b2down
  battery2.hideturtle()
  battery2.clear()
  b2down = True
  for i in range(0, len(missile2)):
      missile2[i].hideturtle()
      missile2[i].clear()
  for i in range(0, len(b2missile)):
      b2missile[i][0].hideturtle()
      b2missile[i][0].clear()

def battery3down():
  global b3down
  battery3.hideturtle()
  battery3.clear()
  b3down = True
  for i in range(0, len(missile3)):
      missile3[i].hideturtle()
      missile3[i].clear()
  for i in range(0, len(b3missile)):
      b3missile[i][0].hideturtle()
      b3missile[i][0].clear()

end = time.time()+1
def enemyhitbattery(t, x, y, b, bx, by,cursorx,cursory):  # enemy, x cor, ycor, battery, xcor, ycor
  global end
  d = t.distance(bx, by)
  if d < 20:
      if x<-220:
          battery1down()
      elif -220<x<220:
          battery2down()
      elif x>220:
          battery3down()
      t.hideturtle()
      t.clear()
      t.penup()
      while time.time() < end:
          cursorboy.goto(cursorx,cursory)
      finish[enemy.index(t)]=0

def levelup():
  global finish,level,numberofenemy,enemyspeed
  if sum(finish)==0:
      levelboy.clear()
      level+=1
      if numberofenemy<9 and (level-1)%2==0:
          numberofenemy+=1
      levelboy.write("LEVEL " + str(level), font=("Courier", 25, "bold"), align="center")
      enemyspeed+=0.25
      finish.clear()
      enemy.clear()
      for i in range(0, numberofenemy):
          finish.append(1)
      spawnenemy()

cdown = [1,1,1,1,1,1]

def enemyhitcity(t, x, y, c, cx, cy):  # enemy, x cor, ycor, city, xcor, ycor
  global life, cdown,finish
  d = t.distance(cx, cy)
  if d < 5 and cdown[cities.index(c)]==1:  #enemy missile size=1
      c.hideturtle()
      life -= 1
      lifeboy.clear()
      lifeboy.write("Lives: " + str(life), font=("Courier", 15, "bold"), align="left")
      t.hideturtle()
      t.clear()
      t.penup()
      cdown[cities.index(c)]=0
      finish[enemy.index(t)]=0
  elif d < 5 and cdown[cities.index(c)]==0:
      t.hideturtle()
      t.clear()
      t.penup()
      finish[enemy.index(t)]=0

enemy = []
targets = [battery1,battery2,battery3,cities[0],cities[1],cities[2],cities[3],cities[4],cities[5]]
assigned = []

def shot(player, playerx,playery,e,enemyx,enemyy):
  global score, finish,bullet1finish,bullet2finish,bullet3finish
  d = e.distance(playerx, playery)
  if d <= 40 and finish[enemy.index(e)]==1:
      score+=1000
      scoreboy.clear()
      scoreboy.write("Score: " + str(score), font=("Courier", 15, "bold"), align="left")
      e.hideturtle()
      e.clear()
      e.penup()
      player.clear()
      player.shape("circle")
      player.penup()
      finish[enemy.index(e)]=0
      for i in range(0,len(b1missile)):
           if player in b1missile[i]:
               bullet1finish[i]=0
               b1missile[i][3]=True
      for i in range(0,len(b2missile)):
           if player in b2missile[i]:
               bullet2finish[i]=0
               b2missile[i][3] = True
      for i in range(0,len(b3missile)):
           if player in b3missile[i]:
               bullet3finish[i]=0
               b3missile[i][3]=True

def spawnenemy(): #spawn enemy based on set # of enemy and assign a target to
  global assigned,enemy, finish
  for i in range(0, numberofenemy):
      enemy.append(turtle.Turtle())
      enemy[i].hideturtle()
      enemy[i].penup()
      enemy[i].color("#ff0000")
      enemy[i].turtlesize(1)
      enemy[i].setheading(270)
      enemy[i].pensize(2)
      enemy[i].goto(random.randint(-300, 300), 300)
      enemy[i].pendown()
      enemy[i].showturtle()
  for j in range(0,len(enemy)): #add enough targets to assigned targets to accommodate for every enemy
      rand = random.randint(0,8)
      assigned.append(targets[rand])
  for i in range(0,len(assigned)): #if any targets are dupes, reassign
      for j in range(0,len(assigned)):
          while i!=j and assigned[j]==assigned[i]:
              rand = random.randint(0, 8)
              assigned[i] = targets[rand]

enemyspeed=1

def enemyfire(t, x, y): # enemy missile go towards target
  global enemyspeed
  if finish[enemy.index(t)]==1 and t.ycor() != y and t.xcor() != x:
      t.setheading(t.towards(x, y))
      t.forward(enemyspeed)

startexplodetime = 0

def pointreach(t,x,y):
   global b1missile, b2missile,b3missile, startexplodetime
   if x - 10 <= t.xcor() <= x + 10 and y - 10 <= t.ycor() <= y + 10:
       t.shape("circle")
       startexplodetime = time.time()
       for i in range(0, len(b1missile)):
           if t in b1missile[i]:
               bullet1finish[i]=0
               b1missile[i][3]=True
       for i in range(0, len(b2missile)):
           if t in b2missile[i]:
               bullet2finish[i]=0
               b2missile[i][3]=True
       for i in range(0, len(b3missile)):
           if t in b3missile[i]:
               bullet3finish[i] = 0
               b3missile[i][3]=True
       t.clear()

def follow():
  global x,y,lowestpoint
  if (y * -1) + 400 > lowestpoint:
      cursorboy.setposition(x - 400, (y * -1) + 400)
  else:
      cursorboy.setposition(x - 400, lowestpoint)

def spacebar():
   global life, b1down, b2down, b3down, cdown
   if life>1:
       if b1down == True:
           for i in range(0,len(cities)):
               if cdown[i]==1:
                   cdown[i]=0
                   cities[i].hideturtle()
                   break
           life -= 1
           lifeboy.clear()
           lifeboy.write("Lives: " + str(life), font=("Courier", 15, "bold"), align="left")
           b1down=False
           battery1.showturtle()
           for i in range(0, len(missile1)):
               missile1[i].showturtle()
       elif b2down == True:
           for i in range(0,len(cities)):
               if cdown[i]==1:
                   cdown[i]=0
                   cities[i].hideturtle()
                   break
           life -= 1
           lifeboy.clear()
           lifeboy.write("Lives: " + str(life), font=("Courier", 15, "bold"), align="left")
           b2down=False
           battery2.showturtle()
           for i in range(0, len(missile2)):
               missile2[i].showturtle()
       elif b3down == True:
           for i in range(0,len(cities)):
               if cdown[i]==1:
                   cdown[i]=0
                   cities[i].hideturtle()
                   break
           life -= 1
           lifeboy.clear()
           lifeboy.write("Lives: " + str(life), font=("Courier", 15, "bold"), align="left")
           b3down=False
           battery3.showturtle()
           for i in range(0, len(missile3)):
               missile3[i].showturtle()

# ---------------------------
mywindow.onclick(setup)
mywindow.listen()
mywindow.onkeypress(spacebar, "space")
screen = mywindow.getcanvas()
x = 400
y = 400
s1 = 3
s2 = 3
s3 = 3
lowestpoint = -130  # change according to structures
FPS = 60  #60 frames per second
refreshAt = 1/FPS #and so this is the refresh interval
startOfInterval = time.time()
mywindow.tracer(0,0)
#GAME--------------------------------------------------------------------

while life > 0 and sum(cdown)>0:
  endOfInterval = time.time()
  endexplodetime = time.time()
  if endOfInterval - startOfInterval >= refreshAt:
      follow()
      cursorboy.onclick(click)
      if b1down == False:
          for i in range(0,len(b1missile)):
              if bullet1finish[i]==1:
                  b1missile[i][0].setheading(b1missile[i][0].towards(b1missile[i][1],b1missile[i][2]))
                  if b1missile[i][0].xcor()!=b1missile[i][1] and b1missile[i][0].ycor()!=b1missile[i][2] and bullet1finish[i]==1:
                      b1missile[i][0].forward(10)
                  for z in range(0,len(enemy)):
                      shot(b1missile[i][0], b1missile[i][0].xcor(), b1missile[i][0].ycor(), enemy[z], enemy[z].xcor(),enemy[z].ycor()) #if player missile hit enemy missile
                  pointreach(b1missile[i][0],b1missile[i][1],b1missile[i][2]) #check if my missile reached point
              if endexplodetime-startexplodetime>=refreshAt and b1missile[i][3]==True:
                  b1missile[i][0].turtlesize(b1missile[i][4])
                  b1missile[i][4]-=0.1
                  if b1missile[i][4] <= 0:
                      b1missile[i][0].hideturtle()
                      b1missile[i][3] = False
      if b2down == False:
          for i in range(0,len(b2missile)):
              if bullet2finish[i] == 1:
                  b2missile[i][0].setheading( b2missile[i][0].towards( b2missile[i][1],  b2missile[i][2]))
                  if b2missile[i][0].xcor()!=b2missile[i][1] and b2missile[i][0].ycor()!=b2missile[i][2] and bullet2finish[i]==1:
                      b2missile[i][0].forward(10)
                  for z in range(0,len(enemy)):
                      shot(b2missile[i][0], b2missile[i][0].xcor(), b2missile[i][0].ycor(), enemy[z], enemy[z].xcor(),enemy[z].ycor())  # if player missile hit enemy missile
                  pointreach(b2missile[i][0], b2missile[i][1], b2missile[i][2])  # check if my missile reached point
              if endexplodetime-startexplodetime>=refreshAt and b2missile[i][3]==True:
                  b2missile[i][0].turtlesize(b2missile[i][4])
                  b2missile[i][4]-=0.1
                  if b2missile[i][4] <=0:
                      b2missile[i][0].hideturtle()
                      b2missile[i][3] = False
      if b3down == False:
          for i in range(0,len(b3missile)):
              if bullet3finish[i] == 1:
                  b3missile[i][0].setheading( b3missile[i][0].towards( b3missile[i][1],  b3missile[i][2]))
                  if b3missile[i][0].xcor()!=b3missile[i][1] and b3missile[i][0].ycor()!=b3missile[i][2] and bullet3finish[i]==1:
                      b3missile[i][0].forward(10)
                  for z in range(0, len(enemy)):
                      shot(b3missile[i][0], b3missile[i][0].xcor(), b3missile[i][0].ycor(), enemy[z], enemy[z].xcor(),enemy[z].ycor())  # if player missile hit enemy missile
                  pointreach(b3missile[i][0], b3missile[i][1], b3missile[i][2])  # check if my missile reached point
              if endexplodetime - startexplodetime >= refreshAt and b3missile[i][3] == True:
                  b3missile[i][0].turtlesize(b3missile[i][4])
                  b3missile[i][4] -= 0.1
                  if b3missile[i][4] <= 0:
                      b3missile[i][0].hideturtle()
                      b3missile[i][3] = False
      for i in range(0, len(enemy)):
          enemyfire(enemy[i], assigned[i].xcor(), assigned[i].ycor())  # enemy missiles move towards select targets
          enemyhitbattery(enemy[i], enemy[i].xcor(), enemy[i].ycor(), battery1, b1x, b1y,cursorboy.xcor(), cursorboy.ycor()) #check to see if missile hit battery
          enemyhitbattery(enemy[i], enemy[i].xcor(), enemy[i].ycor(), battery1, b2x, b2y,cursorboy.xcor(), cursorboy.ycor())
          enemyhitbattery(enemy[i], enemy[i].xcor(), enemy[i].ycor(), battery3, b3x, b3y,cursorboy.xcor(), cursorboy.ycor())
          follow()
          for z in range (0,len(cities)):
              if finish[enemy.index(enemy[i])]==1:
                   enemyhitcity(enemy[i], enemy[i].xcor(), enemy[i].ycor(), cities[z], cities[z].xcor(), cities[z].ycor()) #check to see if missile hit city
      levelup()
      mywindow.update()  # manually draw the screen
      startOfInterval = time.time()

cursorboy.hideturtle()
lifeboy.clear()
levelboy.clear()
scoreboy.clear()
terrainboy.clear()
hideboy.stamp()
for i in range(0,len(enemy)):
   enemy[i].clear()
   enemy[i].hideturtle()
battery1down()
battery2down()
battery3down()
writerboy.color("white")
writerboy.goto(0,0)
writerboy.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
time.sleep(2)
writerboy.clear()
writerboy.write("Final Score: "+str(score), font=("Courier", 30, "bold"), align="center")
time.sleep(3)
writerboy.clear()
writerboy.write("Thanks for playing!", font=("Courier", 30, "bold"), align="center")
time.sleep(3)
mywindow.bye()

mywindow.mainloop()
