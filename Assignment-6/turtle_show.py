import turtle

p = turtle.Pen()
p.shape("turtle")
p.speed(2.5)
turtle.bgcolor("white")
p.pencolor('black')
p.width(1.5)
p.penup()
p.pendown()

i, j = 0, 0
side=0

while i < 10:
    
    degree = ( ((i+3-2)*180) / (i+3) )
    p.left(180 - (degree / 2))
    side += 106

    while j <= i+2:
        p.forward( side / (i+3) )
        p.left(180 - degree)
        j += 1

    p.penup()
    p.right(180 - degree)
    p.right(degree / 2)
    p.forward(17)
    p.pendown()
    j=0
    i+=1