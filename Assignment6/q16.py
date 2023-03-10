#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def case(str):
    c,c1=0,0
    for i in str:
        if ord(i)>=65 and ord(i)<=90:
            c+=1
        if ord(i)>=97 and ord(i)<=122:
            c1+=1
    print("Number of upper case letters:",c)
    print("Number of lower case letters:",c1)
string=input("Enter a string:")
case(string)