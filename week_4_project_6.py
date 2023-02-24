import math
number = float(input("Enter the number of iterations: "))
div = -3
while number != 0:
     div = float(div)

     number -= 1

     pi = 1 - (1/div)

     div = 3 + 2

print(pi)
print(div)
