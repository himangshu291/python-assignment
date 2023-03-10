#Program to print all numbers which are divisible by M and N in the List.
list=input("Enter the list elements:").split()
list1=[int(i) for i in list]
m=int(input("Enter the value of m:"))
n=int(input("Enter the value of n:"))
res=[]
for i in list1:
    if i%m==0 and i%n==0:
        res.append(i)
print("All numbers which are divisible by M and N in the List are:",res)