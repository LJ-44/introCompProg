import random
import turtle
import dth

r1, g1, b1 = random.random(), random.random(), random.random()
r2, g2, b2 = random.random(), random.random(), random.random()

print(f'rgb({int(r1*255)}, {int(g1*255)}, {int(b1*255)})')
print(f'hex code: #{str(dth.decimalToHex(int(r1*255))) + str(dth.decimalToHex(int(g1*255))) + str(dth.decimalToHex(int(b1*255)))}')

wn = turtle.Screen()
t = turtle.Turtle()
t.color(r1, g1, b1)
t.shape("circle")
t.shapesize(80)
wn.exitonclick()