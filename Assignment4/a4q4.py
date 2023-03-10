n=input("Enter a string:")
c=0
for i in n:
    if(i==" "):
        continue
    else:
        c+=1
print("Length of a string:",c)