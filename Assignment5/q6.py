#Program to remove first occurrence of a given element in the list.
list=input("Enter the list of values:").split()
list1=[int(i) for i in list]
print(list1)
item=int(input("Enter the item to be deleted:"))
list1.remove(item)
print("After removing first occurance of a given element:")
print(list1)