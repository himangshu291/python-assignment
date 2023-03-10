#Write a program to split and join a string
str1=input("Enter a string: ").split()
print("Split String:",str1)
str2=""
for i in str1:
    str2=' '.join(str1)
print("Join String:",str2)    