a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
print(f"All armstrong no.s between {a} and {b}:")
for i in range(a,b+1):
    n=i
    s=0
    while(n>0):
        d=n%10
        s=s+d*d*d
        n=n//10
    if(s==i):
        print(i)