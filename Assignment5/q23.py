#Create two lists with first half and second half elements of a list.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
res=list1[ :len(list1)//2]
print("First half elements are:",res)
res1=list1[len(list1)//2: ]
print("Second half elements are:",res1)


'''
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
res=[]
res1=[]
i=0
if len(list1)%2==0:
    while i<=(len(list1)//2)-1:
        res.append(list1[i])
        i+=1
    j=len(list1)//2
    while j<len(list1):
        n=list1[j]
        res1.append(list1[j])
        j+=1
else:
    while i<=(len(list1)//2):
        res.append(list1[i])
        i+=1
    j=len(list1)//2+1
    while j<len(list1):
        res1.append(list1[j])
        j+=1
print("First half elements are:",res)
print("Second half elements are:",res1)
'''