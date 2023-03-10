#Create three lists of numbers, their squares and cubes.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
res=[]
res1=[]
for i in list1:
    res.append(i*i)
    res1.append(i*i*i)
print("List of numbers are:",list1)
print("List of their squares are:",res)
print("List of their cubes are:",res1)
    