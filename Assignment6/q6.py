#Write a Python program to understand the use of asterisk(*) character declared in a function.
def mul(x,y):
    r=x*y
    return r
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=mul(a,b)
print("Multiply of two numbers =",s)