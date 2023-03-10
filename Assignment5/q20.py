#print list after removing EVEN numbers.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
for i in list1:
    if i%2==0:
        list1.remove(i)
print("List after removing EVEN numbers are:",list1)        
