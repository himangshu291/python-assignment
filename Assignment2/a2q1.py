yr=int(input("Enter a year: "))
if(yr%100==0) and (yr%400==0):
    print("{} is a leap year".format(yr))
elif(yr%4==0) and (yr%100!=0):
    print("{} is a leap year".format(yr))
    #print("The year %d is a leap year"%yr)
    #print("The year",yr,"is a leap year")
else:
    print(f"{yr} is not a leap year")
