n=int(input("Enter the number of terms you want to add:"))
f=1
s=0
for i in range(1,n+1):
    f=f*i
    r=i/f
    s=s+r
print("The Sum of first seven terms:",s)