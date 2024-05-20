import turtle
pen = turtle.Turtle() #画笔对象
radius = [x*2  for x in range(1,40) if x % 5 == 0]
my_colors = ("red", "blue", "green", "yellow", "orange", "purple", "brown")
for r,i in zip(radius,range(len(radius))):
    pen.penup()#抬笔
    pen.goto(0,-r)
    pen.pendown()
    pen.color(my_colors[i%len(my_colors)])
    pen.circle(r)
print(radius)
turtle.done()#程序执行完毕窗口依然存在
