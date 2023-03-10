'''n=int(input("Enter a number: "))
f=1
if(n==0):
    print("Factorial=1")
else:
    for i in range(1,n+1):
        f=f*i
    print("Factorial=",f)
    '''
T=int(input())
for i in range(T):
    n=int(input())
    s=0
    t=n
    while(n>0):
        d=n%10
        s=s*10+d
        n=n//10
    if s==t :
        print("wins")
    else :
        print("loses")