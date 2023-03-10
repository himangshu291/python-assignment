#Write a Python function that checks whether a passed string is palindrome or not.
def palin(str):
    i=len(str)-1
    res=''
    while (i>=0):
        res+=str[i]
        i-=1
    return res
str=input("Enter a string:")
if palin(str)==str:
    print("Palindrome")
else:
    print("Not a palindrome")
