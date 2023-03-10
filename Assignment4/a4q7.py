#Write a program to capitalize the first and last character of each word in a string
res=input("Enter a string:").split(' ')
t=''
for i in res:
    if len(i)==1 :
        t=t+i[0].upper()+" "
    else:
        t=t+i[0].upper()+i[1:-1]+i[-1].upper()+" "
print(t) 