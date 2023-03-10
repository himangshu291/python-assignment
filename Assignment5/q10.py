#Convert a string to integers list.
list=input("Enter a number as a string:").split()
print("The String is:",list)
list1=[int(i) for i in list]
print ("Modified list is : " + str(list1))