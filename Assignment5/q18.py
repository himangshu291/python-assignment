#Program to remove duplicate elements from the list.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
res=[]
for i in list1:
    if i not in res:
        res.append(i)
print("After remove all duplicate elements from the list:",res)