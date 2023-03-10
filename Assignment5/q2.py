#Python program to print list elements in different ways.
l=['a','e','i','o','u']
for i in range(len(l)):
    print(l[i],end=" ")
print()
for i in l:
    print(i,end=" ")
print()
print(*l, end=" ")
print()
print(''.join(l))
