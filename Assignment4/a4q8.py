#Python program to check if a string has at least one letter and one number
'''
str=input("Enter a string:")
if str.isalpha():       #isalpha find the alphabet
    print(str,"contains alphabet")
elif str.isdigit():     #isdigit find the number
    print(str,"contains number")
elif str.isalnum():     #isalnum is used to find alphabet & number both
    print("The string",str,"contains number and letters")
else:
    print("Wrong Entry")
'''
str=input("Enter a string: ")
i,nc,nd=0,0,0
while(i<len(str)):
    a=ord(str[i])
    if a>=97 and a<=122 or a>=65 and a<=90:
        nc+=1
    if a>=48 and a<=57:
        nd+=1
    if nc>=1 and nd>=1:
        break
    i+=1
if (nc>=1 and nd>=1):
    print("letters and digits found")
else:
    print("Not found")
