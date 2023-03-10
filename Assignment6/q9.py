#Create a function to calculate and return HCF of two numbers.
def hcf(a,b):  
    max=a if(a>b) else b        #conditional operator
    min=a if(a<b) else b
    r=max%min
    while(r!=0):
        max=min
        min=r
        r=max%min
    gcd=min             #gcd=hcf
    return gcd
n1=int(input("Enter first number: "))  
n2=int(input("Enter second number: "))  
print("The H.C.F. of",n1,"and",n2,"is",hcf(n1,n2))