a=int(input("Enter first side of a triangle: "))
b=int(input("Enter second side of a triangle: "))
c=int(input("Enter third side of a triangle: "))
if(a==b and b==c):
       print("It is a equilateral triangle")
elif (a==b or b==c or c==a):
       print("It is a isoceles triangle")
elif ((a**2)==((b**2)+(c**2))):
       print("It is a right angled triangle") 
else:
       print("It is a scalene triangle")

