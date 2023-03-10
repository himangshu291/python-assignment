#Write a program to remove all the duplicates of a given string in python,keeping the first characters only.
str=input("Enter the string:")
str1=""
for i in str:
    if i not in str1:
        str1=str1+i 
print("After removing all duplicates characters:",str1)