#Write a program to minimum frequency characters in String
str1=input("Enter a string:")
min=str1[0]
i=1
while i<len(str1):
    if str1.count(str1[i])<str1.count(min):
        min=str1[i]
    i=i+1
print(min,"is the least frequent charecter with frequency of",str1.count(min)) 