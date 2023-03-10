'''
n=int(input("Enter a four digit number: "))
d1=n%10
d4=n//1000
s=d1+d4
print("The sum of digits= ",s) 
'''

n=input("Enter a four digit number: ")
l=len(n)
s=0
while(l>0):
    if(l==4 or l==1):
        d=n%10
        s=s+d
l=l-1
print("The sum of digits= ",s) 
