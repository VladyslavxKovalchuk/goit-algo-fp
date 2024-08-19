import turtle
import math


def draw_tree(turtle_obj, length, depth):
    if depth == 0:
        return

    turtle_obj.forward(length)

    turtle_obj.right(45)
    draw_tree(turtle_obj, length / math.sqrt(2), depth - 1)

    turtle_obj.left(90)
    draw_tree(turtle_obj, length / math.sqrt(2), depth - 1)

    turtle_obj.right(45)
    turtle_obj.backward(length)


def main():
    depth = int(input("Вкажіть рівень рекурсії:"))
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Дерево Піфагора")

    fractal_turtle = turtle.Turtle()
    fractal_turtle.speed(0)
    fractal_turtle.left(90)
    fractal_turtle.penup()
    fractal_turtle.goto(0, -200)
    fractal_turtle.pendown()

    draw_tree(fractal_turtle, 100, depth)
    turtle.done()


if __name__ == "__main__":
    main()
