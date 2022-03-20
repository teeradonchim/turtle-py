Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
for i in range(10):
    tao.circle(50)
    tao.left(36)

    
Go(100,100)
range()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    range()
TypeError: range expected at least 1 argument, got 0
range(10)
range(0, 10)
