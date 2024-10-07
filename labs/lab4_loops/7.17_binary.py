#This code prints the reverse binary of a decimal user input integer

x = int(input())

while x > 0:
    print(x % 2, end='')
    x //= 2