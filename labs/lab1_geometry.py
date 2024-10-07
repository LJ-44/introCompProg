print('''This program will calculate all of the coordinates
for the corners of a rectangle.
But first you will need to enter a little data.''')

xC = int(input("Enter the x coordinate for the lower left corner of the rectangle:\t"))
yC = int(input("Enter the y coordinate for the lower left corner of the rectangle:\t"))
print()

w = int(input("Enter the width of the rectangle:\t"))
h = int(input("Enter the height of the rectangle:\t"))
print()

print('Here are your results.')
print(f'Upper Left Corner Coordinates:\t({xC},{yC + h})')
print(f'Upper Right Corner Coordinates:\t({xC + w},{yC + h})')
print(f'Lower Left Corner Coordinates:\t({xC},{yC})')
print(f'Lower Right Corner Coordinates:\t({xC + w},{yC})')