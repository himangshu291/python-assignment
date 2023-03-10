n=input("Enter a string: ").split()
print("Even length words are: ")
for i in n:
    if len(i)%2==0:
        print(i)