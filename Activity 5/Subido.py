import turtle 
colors = ['green' , 'red' , 'blue' , 'orange' 'yellow']
p = turtle.Pen()
turtle.bgcolor('black')
for i in range(368)
    p.pencolor(colors[i%6])
    p.width(i//100 + 1)
    p.format(i)
    p.left(59)
