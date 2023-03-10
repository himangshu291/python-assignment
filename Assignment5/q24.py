#print list after removing ODD numbers.
list1=input("Enter the list elements:").split()
#list=[11, 22, 33, 44, 55]
list=[int(i) for i in list1]
print(list)
i=0
#while i<len(list)-1:
for i in list:
    if (i%2!=0):
        list.remove(i)
print("List after removing ODD numbers are:",list)