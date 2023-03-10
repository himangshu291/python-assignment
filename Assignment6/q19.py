# Write a Python program to print the even numbers from a given list.
def even(l):
    l2=[int(i) for i in l]
    res=[]
    for i in l2:
        if i%2==0:
            res.append(i)
    return res
l1=input("Enter a list of elements:").split()
print("Even numbers are:",even(l1))     