#Create a list from the specified start to end index of another list.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
s=int(input("Enter the starting index:"))
e=int(input("Enter the ending index:"))
if (s<0):
    print ("Invalid start index")
if(e>len(list1)-1):
    print("Invalid end index")
res=list1[s:e+1]
print("List of specified start to end index are:",res)