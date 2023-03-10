n=int(input("How many numbers you want to enter:"))
pos=0
neg=0
zero=0
i=0
while(i<n):
    num=int(input("Enter the numbers:"))
    if(num>0):
        pos+=1
    elif(num<0):
        neg+=1
    elif(num==0):
        zero+=1
    i+=1
print(f"The positive numbers={pos}, negative numbers={neg},zero={zero}")