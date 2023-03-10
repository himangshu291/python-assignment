#Write a program to add two integers using function.
def add(x,y):
    r=x+y
    return r
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=add(a,b)
print("Sum =",s)