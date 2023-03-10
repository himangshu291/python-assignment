'''
import array    
n=int(input("Enter how many number you want to enter: "))
a=array.array('i',[])
for i in range(n):
    num=int(input("Enter the number: "))
    a.append(num)
max=a[0]
min=a[0]
for i in range(1,n):
    if(a[i]>max):
        max=a[i]
#print(max)
for i in range(1,n):
    if(a[i]<min):
        min=a[i]     
#print(min)
print("Range is: ",max-min)
        
        
        
         
        
        
maximum = minimum = num
for i in range(1,how):
    num = int(input("Enter the number :"))
    if(num>maximum):
        maximum = num
    if(num<minimum):
        minimum = num
r = maximum-minimum
print("Range is:",r)
'''
l=input("Enter the list of elements:").split()
l1=[int(i) for i in l]
min=l1[0]
max=l1[0]
for i in l1:
    if i>max:
        max=i
    if i<min:
        min=i
print("Range is: ",max-min)

        