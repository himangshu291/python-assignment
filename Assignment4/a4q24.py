#Write a program to swap commas and dots in a String
str=input("Enter a string: ")
str1=''
for i in str:
    if i=='.':
        str1+=','
    elif i==',':
        str1+='.'
    else:
        str1+=i
print("After swapping comma and dots:",str1)
    