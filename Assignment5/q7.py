#Remove all occurrences a given element from the list.
list=input("Enter the list of values:").split()
list1=[int(i) for i in list]
print(list1)
item=int(input("Enter the item to be deleted:"))
i=0
while i<len(list1)-1:
    c=list1.count(item)
    print(c)
    if c>=1:
        list1.remove(item)
    i+=1
# list1.remove(item)
print("After removing all the occurance of a given element:")
print(list1)