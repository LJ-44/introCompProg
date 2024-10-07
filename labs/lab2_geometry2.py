xC = int(input("Enter the x coordinate for the lower left corner of the rectangle:\t"))
yC = int(input("Enter the y coordinate for the lower left corner of the rectangle:\t"))
print()

w = int(input("Enter the width of the rectangle:\t"))
h = int(input("Enter the height of the rectangle:\t"))
print()

x = int(input("Enter the x coordinate of the point:\t"))
y = int(input("Enter the y coordinate of the point:\t"))

#Checking if the point is on the rectangle using the x,y inputs
if (
    (xC <= x <= (xC + w) and y == yC) or
    (yC <= y <= (yC + h) and x == xC) or
    (xC <= x <= (xC + w) and y == (yC + h)) or
    (yC <= y <= (yC + h) and x == (xC + w))
   ):
    print("On the rectangle")
#Checking if the point is inside the rectangle using the x,y inputs
elif ((x > yC and x < (xC + w)) and (y > yC and y < (yC + h))):
    print("Inside the rectangle")
#If the point is neither on or inside the rectangle, it must be outside of it
else:
    print("Outside the rectangle")