'''
n=input("Enter a string:")
l=len(n)
h=l/2
print("Uppercase of Half string is:")
for i in range(int(l)):
    if i<h :
        print(n[i].upper(),end=' ')
    else:
        print(n[i],end=" ")
'''
str=input("Enter a string:")
l=len(str)
print(l)
if(l%2==0):
    a=str[:l//2]
    b=str[l//2:]
else:
    a=str[:l//2+1]
    b=str[l//2+1:]
res=a.upper()+b
print(res)