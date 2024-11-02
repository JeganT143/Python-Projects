import turtle
import math

def drawKochSF(x1, y1, x2, y2, t, color):
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    r = d / 3.0
    h = r * math.sqrt(3.0) / 2
    p3 = ((x1 + 2 * x2) / 3, (y1 + 2 * y2) / 3)
    p1 = ((2 * x1 + x2) / 3, (2 * y1 + y2) / 3)
    c = (0.5 * (x1 + x2), 0.5 * (y1 + y2))
    n = ((y1 - y2) / d, (x2 - x1) / d)
    p2 = (c[0] + h * n[0], c[1] + h * n[1])

    if d > 30:
        drawKochSF(x1, y1, p1[0], p1[1], t, color)
        drawKochSF(p1[0], p1[1], p2[0], p2[1], t, color)
        drawKochSF(p2[0], p2[1], p3[0], p3[1], t, color)
        drawKochSF(p3[0], p3[1], x2, y2, t, color)
    else:
        t.color(color)
        t.up()
        t.setpos(x1, y1)
        t.down()
        t.goto(p1[0], p1[1])
        t.goto(p2[0], p2[1])
        t.goto(p3[0], p3[1])
        t.goto(x2, y2)

def drawSnowflake(x, y, size, angle, t, colors):
    # Rotate the entire snowflake by a specified angle
    t.up()
    t.setpos(x, y)
    t.down()
    t.seth(angle)

    # Calculate vertices of an equilateral triangle
    point1 = (x - size / 2, y - math.sqrt(3) * size / 6)
    point2 = (x + size / 2, y - math.sqrt(3) * size / 6)
    point3 = (x, y + math.sqrt(3) * size / 3)

    # Draw each side of the Koch Snowflake with a different color
    drawKochSF(point1[0], point1[1], point2[0], point2[1], t, colors[0])
    drawKochSF(point2[0], point2[1], point3[0], point3[1], t, colors[1])
    drawKochSF(point3[0], point3[1], point1[0], point1[1], t, colors[2])

def main():
    print("Drawing a symmetrical Koch Snowflake pattern with a central snowflake")
    screen = turtle.Screen()
    screen.bgcolor("black")
    
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)  # Fastest speed
    t.width(2)  # Consistent line width for symmetry

    # Colors for a gradient-like effect
    colors_list = [
        ["#FF6347", "#FFD700", "#ADFF2F"],  # Gradient 1
        ["#87CEEB", "#FF69B4", "#BA55D3"],  # Gradient 2
        ["#32CD32", "#40E0D0", "#FFD700"],  # Gradient 3
    ]

    # Draw central snowflake
    center_size = 150  # Size for the central snowflake
    center_colors = ["#FF6347", "#FFD700", "#32CD32"]  # Unique colors for the center
    drawSnowflake(0, 0, center_size, 0, t, center_colors)

    # Define the number of snowflakes and angle step for surrounding pattern
    num_snowflakes = 6
    radius = 200  # Radius from the center
    angle_step = 360 / num_snowflakes

    # Draw each surrounding snowflake evenly around the central snowflake
    for i in range(num_snowflakes):
        angle = i * angle_step
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        size = 100  # Fixed size for symmetry in surrounding snowflakes
        colors = colors_list[i % len(colors_list)]
        
        drawSnowflake(x, y, size, angle, t, colors)

    screen.exitonclick()

if __name__ == "__main__":
    main()
