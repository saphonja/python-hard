import turtle

def draw_square(turtle_sq):
    for i in range (1,5):
        turtle_sq.forward(100)
        turtle_sq.right(90)

def draw_circle(turtle_circle):
    for i in range (1,121):
        draw_square(turtle_circle)
        turtle_circle.right(3)

def draw_triangle(turtle_triangle):
    for i in range (1,4):
        turtle_triangle.left(40)
        turtle_triangle.right(60)

def draw_flower(flower):
    flower.forward(100)
    for i in range (1,31):
        draw_triangle(flower)
        flower.right(6)

    window.exitonclick()

def draw_art():
    window = turtle.Screen()
    window.bgcolor("green")
    #draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)
    draw_flower(brad)

    #draw a circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
draw_art()
