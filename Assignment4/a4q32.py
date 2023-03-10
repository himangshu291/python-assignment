#Write a program to sort String list by K character frequency
#Using sorted() + count() + lambda

str=input("Enter a sentence:").split()
#list=["I", "am","from","siliguri"]
str1=''
str2=''
# printing original list
print("The original list is: ",str)
k=input("Enter the k-th character:")
# "-" sign used to reverse sort
#res=sorted(list, key = lambda ele: -ele.count(k))
for i in str:
    if k in i:
        str1+=i+' '
    else:
        str2+=i+' '
str1+=str2
# printing results
print(f"Sorted String list:{str1}")