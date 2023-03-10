#Write a Python program to understand the use of double asterisk(*) character declared in a function.
def pow(x,y):
    r=x**y
    return r
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=pow(a,b)
print("{} Power {} is {}".format(a,b,s))
print(f"{a} Power {b} is {s}")