print("Find the Library fine")
days=int(input("Enter the number of days member is late to return the book: "))
if(days>=1 and days<=5):
      print("Fine is 50 paise")
elif(days>=6 and days<=10):
      print("Fine is 1 rupee")
elif(days>10 and days<=30):
      print("Fine is 5 rupee")
elif(days>30):
      print("Your membrship will be cancelled")
else:
      print("Please enter the correct number of days")