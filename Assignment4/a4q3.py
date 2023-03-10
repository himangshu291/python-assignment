str=input("Enter a string: ")
a=int(input("Enter the ith character you want to remove: "))
b=str[0:a]
c=str[a+1: ]
str=b+c
print("new String:",str)

#another method
str=input("Enter a string: ")
a=int(input("Enter the ith character you want to remove: "))
new_str=" "
for i in range(len(str)):
    if i!=a:
        new_str=new_str+str[i]
print("new String:",new_str)