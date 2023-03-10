#Program to Print the index of first matched element of a list.
list=input("Enter a list of values:").split()
list1=[int(i) for i in list]
l=[]
i=0
while i<len(list1):
    if list1[i] in l:
        print("The index of first matched element:",i)
        break
    else:
        l.append(list1[i])
    i+=1
list1.sort()
l.sort()
if list1==l:
    print("No matched element in a list")