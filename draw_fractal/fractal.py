import turtle
import math
def drawKochSF(x1,y1,x2,y2,t):
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    r = d/3.0
    h = r*math.sqrt(3.0)/2
    p3 = ((x1+2*x2)/3,(y1+2*y2)/3)
    p1 = ((2*x1+x2)/3, (2*y1+y2)/3)
    c = (0.5*(x1+x2), 0.5*(y1+y2))
    n = ((y1-y2)/d , (x2-x1)/d)
    p2 =(c[0]+h*n[0], c[1]+h*n[1])
    
    if d > 10:
        drawKochSF(x1,y1,p1[0],p1[1],t)
        drawKochSF(p1[0],p1[1],p2[0],p2[1],t)
        drawKochSF(p2[0],p2[1],p3[0],p3[1],t)
        drawKochSF(p3[0],p3[1],x2,y2,t)
    else:
        t.up()
        t.setpos(p1[0],p1[1])
        t.down()
        t.setpos(p2[0],p2[1])
        t.setpos(p3[0],p3[1])
        t.up()
        t.setpos(x1,y1)
        t.down()
        t.setpos(p1[0],p1[1])
        t.up()
        t.setpos(p3[0],p3[1])
        t.down()
        t.setpos(x2,y2)
        

def main():
    print("Drawing the Koch Snowflake")
    t = turtle.Turtle()
    t.hideturtle()
    try:
        drawKochSF(-100,0,100,0,t)
        drawKochSF(0,-173.2,-100,0,t)
        drawKochSF(100,0,0,-173.2,t)
    except:
        print("Exception exiting")
        exit(0)
    turtle.Screen().exitonclick()
    

if __name__ == "__main__":
    main()