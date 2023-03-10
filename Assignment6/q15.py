#Write a Python function to check whether a number falls in a given range.
def range(x):
    a=int(input("Enter the start range:"))
    b=int(input("Enter the end range:"))
    if a<=x<=b:
        print("The number is in range")
    else:
        print("The number out of range")
n=int(input("Enter a number:"))
range(n)