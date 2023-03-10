#Program to remove all elements in a range from the List.
list=input("Enter a list of values:").split()
list1=[int(i) for i in list]
i=int(input("Enter the starting range:"))
j=int(input("Enter the ending range:"))
del list1[i:j]
print(list1)