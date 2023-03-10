#Write a Python function that takes a number as a parameter and check the number is prime or not.
def checkprime(n):
    i=2
    while(i<=n-1):
        if n%i==0:
            break
        i+=1
    if i==n:
        print(n,"is a prime number")
    else:
        print(n,"is not a prime number")
num=int(input("Enter a number: "))
checkprime(num)
