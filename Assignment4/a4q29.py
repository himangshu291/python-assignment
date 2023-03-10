#Write a program to preform string slicing in Python to rotate a string
str=input("Enter a String:")
s=int(input("Enter the rotate index:"))
str1=str
n=str[0:s]
n1=str[s: ]
res=n1+n
m=str1[len(str1)-s: ]
m1=str1[ :len(str1)-s]
res1=m+m1
print("Left Rotation:",res)
print("Right Rotation:",res1)
