n=int(input("Enter the number:"))
oc=0
c=0
temp=n
while n>0:
    oc+=((n%8)*(10**c))
    n=n//8
    c+=1
print(f'octal  of {temp} is {oc}')
