#Write a program to odd Frequency Characters
str1=input("Enter a string:")
str2=""
for i in str1:
    c=str1.count(i)
    if(c%2!=0):
        str2=str2+i+" "
print("The odd frequency characters are:",str2)