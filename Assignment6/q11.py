# Write a Python function to sum all the numbers in a list.d={0:'a',1:'b',2:'c'}
def sumoflist():
    l=input("Enter a list of numbers divided by space: ").split()
    sum=0
    l1=[int(i) for i in l]
    for i in l1:
        sum+=i
    return sum
print("Sum of all numbers in a list: ",sumoflist())
