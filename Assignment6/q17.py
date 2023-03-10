# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(l2):
    l=[int(i) for i in l2]
    res=[]
    for i in l:
        if i not in res:
            #res=res+i
            res.append(i)
    print("Unique elements are:",res)
l1=input("Enter a list divided by space: ").split()
unique_list(l1)
