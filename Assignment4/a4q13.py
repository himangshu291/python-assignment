#Write a program to maximum frequency characters in String
str1=input("Enter a string:")
max=str1[0]
i=1
while i<len(str1):
    if str1.count(str1[i])>str1.count(max):
        max=str1[i]
    i=i+1
print(max,"is the maximum frequent character with frequency of",str1.count(max))