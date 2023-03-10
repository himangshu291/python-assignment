#Write a program to string slicing in Python to check if a string can become empty by recursive deletion
str=input("Enter a String:")
str1=input("Enter a sub String:")
i=0
while i<=len(str):
    i=0
    if str[i] in str1:
        str=str[i+1: ]
    else:
        break
    i+=1
if str=='':
    print("Yes")
if str!='':
    print("No")
'''
Enter a String:lionlion     
Enter a sub String:lion
Yes
'''