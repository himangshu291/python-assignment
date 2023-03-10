# Write a Python program to reverse a string.
def rev():
    str1=''
    i=len(str)-1
    while(i>=0):
        str1+=str[i]
        i-=1
    return str1
str=input("Enter a string:")
print("REverse string is:",rev())