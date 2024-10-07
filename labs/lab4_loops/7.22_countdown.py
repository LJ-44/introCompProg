# This code takes a two digit input, and if both numbers in the two digit number
# are not equal, it counts down by 1 until they are equal, then stops

x = int(input())

if 11 <= x <= 99:
    while str(x)[0] != str(x)[1]:
        print(x)
        x -= 1
    print(x)
else:
    print("Input must be 11-99")
