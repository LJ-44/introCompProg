side1 = int(input())
side2 = int(input())
side3 = int(input())

#max() gets the largest value of the 3 inputs
largest_side = max(side1, side2, side3)

#sorted() sorts the 3 values from smallest to largest, and [0] and [1] are assigned to smallestSide and middleSide
smallest_side, middle_side = sorted([side1, side2, side3])[:2]

if smallest_side + middle_side > largest_side:
    if smallest_side ** 2 + middle_side ** 2 == largest_side ** 2:
        print("These lengths form a right triangle")
    else:
        print("These lengths form a triangle")
else:
    print("These lengths do not form a triangle")