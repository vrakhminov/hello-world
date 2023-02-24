side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

side1 *= (side2 * side2) + (side3 * side3)
side2 *= (side1 * side1) + (side3 * side3)
side3 *= (side1 * side1) + (side2 * side2)

if side3 <= (side1*side1) + (side2*side2):
   print("This triangle is a right triangle.")
else:
   print ("This triangle is not a right triangle.")
