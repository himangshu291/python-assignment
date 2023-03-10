print("Calculate Grade of the steel")
hard=int(input("Enter the Hardness of steel: "))
carb=float(input("Enter the content of carbon of the steel: "))
str=int(input("Enter the Tensile strength of the steel: "))
if((hard>50) and (carb<0.7) and (str>5600)):
        print("Grade is 10")
elif((hard>50) and (carb<0.7)):
        print("Grade is 9")
elif((carb<0.7) and (str>5600)):
        print("Grade is 8")
elif((hard>50)and (str>5600)):
        print("Grade is 7")
elif((hard>50) or (carb<0.7) or (str>5600)):
        print("Grade is 6")
else:
        print("Grade is 5")

