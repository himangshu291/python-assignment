#Write a program for removing i-th character from a string
str=input("Enter a string: ")
i=int(input("Enter the ith character you wqnt to remove: "))
b=str[0:i]
c=str[i+1: ]
str=b+c
print("New String after removing i-th character: ",str)