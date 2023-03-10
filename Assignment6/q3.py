#Create a function to multiply two numbers and the numbers should pass as parameter and return the result.
def mul(x,y):
    r=x*y
    return r
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
s=mul(a,b)
print("Multiply of two numbers =",s)