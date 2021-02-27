import turtle
for i in range(4):
  turtle.seth(90*(i+1))
  turtle.fd(150)
  turtle.right(90)
  turtle.circle(-150,45)
  turtle.goto(0,0)

'''
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,40)
turtle.fd(40)
turtle.circle(16,90)
turtle.fd(40)
'''
turtle.done()
