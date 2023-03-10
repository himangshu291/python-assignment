#Program to input, append and print the list elements.
list=input("Enter the list of elements:").split()
list.append(50)
list.append(90)
list1=[int(i) for i in list]
print(list1)