print("Check valid triangle")
a=float(input("Enter one side of a triangle: "))
b=float(input("Enter second side of a triangle: "))
c=float(input("Enter third side of a triangle: "))
if ((a+b+c==180) and a!=0 and b!=0 and c!=0):
      print("Triangle is valid")
else:
      print("Triangle isn't valid")

