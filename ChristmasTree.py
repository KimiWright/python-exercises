import turtle
tree=turtle.Turtle()
tree.speed(50)
def pine(z,y):
  tree.setpos(z*260.6591307,y*131.059107938)
  tree.pendown()
  for x in range(4):
    tree.fillcolor("green")
    tree.fill(True)
    tree.setheading(0)
    tree.circle(100, -25)
    #print(tree.pos())
    tree.setheading(0)
    tree.circle(100, 40)


  for x in range(4):
    tree.setheading(-40)
    tree.circle(100, 40)
    #print(tree.pos()) (218.397304531, 9.36922129634)
    tree.setheading(25)
    tree.circle(100, -25)
  tree.setheading(0)
  #print(tree.pos()) #(176.135478357, 0.0)
  tree.forward(-180)
  tree.fill(False)
  #print(tree.pos()) #(-3.86452164333, 0.0)
  tree.fillcolor("Brown")
  tree.fill(True)
  tree.forward(70)
  tree.setheading(-90)
  tree.forward(20)
  tree.setheading(0)
  tree.forward(40)
  tree.setheading(90)
  tree.forward(20)
  tree.fill(False)
  #tree.setpos((z+.25)*260.6591307,(y+1)*131.059107938)
  tree.penup()
  tree.sety((y+1)*131.059107938)
  tree.forward(10)
  tree.left(90)
  tree.forward(9)
  tree.left(180)
  tree.pendown()
  tree.fillcolor("yellow")
  tree.pencolor("yellow")
  tree.fill(True)
  for x in range (5):
    tree.right(144)
    tree.forward(20)
  tree.fill(False)
  tree.penup()
  tree.pencolor("black")
def counter(x):
  for z in range(x):
    for y in range(x-z):
      pine(y+.5*z, z)
counter(5)
