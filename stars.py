import turtle
bob=turtle.Turtle()
bob.shape("turtle")#changes shape form arrow
bob.pencolor("blue")
bob.speed("fastest")
#finish with bob.done or turtle.done
for x in range (5):
  bob.forward(100)#goes forward 50 pixels
  bob.right(144)#turns right 90
bob.pencolor("red")
for i in range (50):
  bob.forward(100)
  bob.left(123)
