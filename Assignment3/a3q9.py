def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c+=1
    if(c==2):
        return 1
    else:
        return 0
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"All prime no.s between {a} and {b}:")
for i in range(a,b+1):
    if(prime(i)==1):
        print(i,end=" ")
'''
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"All prime no.s between {a} and {b}:")
c=0
for i in range(a,b+1):
    c=0
    for j in range(2,(i//2+1)):
        if(i%j==0):
            c=c+1
            break
    if(c==0 and i!=1):
        print(i)
'''