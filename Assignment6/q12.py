# Write a Python function to multiply all the numbers in a list
def muloflist():
    l=input("Enter a list of numbers divided by space: ").split()
    mul=1
    l1=[int(i) for i in l]
    for i in l1:
        mul*=i
    return mul
print("Multiply of all numbers in a list: ",muloflist())
