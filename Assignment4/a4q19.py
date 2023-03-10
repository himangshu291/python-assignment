#Write a program to find words that are greater than the given length k
str1=input("Enter Some Words: ").split()
k=int(input("Enter a length: "))
str2=''
for i in str1:
    if len(i)>k:
        str2+=i+" "
print("Words greater than length:",str2)