#Program to Create two lists with EVEN numbers and ODD numbers from a list.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
even=[]
odd=[]
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers list:",even)
print("Odd numbers list:",odd)    