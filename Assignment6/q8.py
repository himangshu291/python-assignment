#Create a function to calculate and return LCM of two numbers.
def lcm(a,b):  
    max=a if(a>b) else b        #conditional operator
    min=a if(a<b) else b
    r=max%min
    while(r!=0):
        max=min
        min=r
        r=max%min
    gcd=min             #gcd=hcf
    lcm=a*b//gcd
    return lcm
n1=int(input("Enter first number: "))  
n2=int(input("Enter second number: "))  
print("The L.C.M. of",n1,"and",n2,"is",lcm(n1,n2))
print(f"The L.C.M. of {n1} and {n2} is",lcm(n1,n2))