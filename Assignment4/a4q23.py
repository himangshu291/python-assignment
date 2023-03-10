#Write a program to find uncommon words from two Strings
str1 = input('Enter first string : ').split()
str2 = input('Enter second string : ').split()
words=''
for i in str1:
    if i not in str2:
        words+=i+' '
for i in str2:
    if i not in str1:
        words+=i+' '
# printing uncommon words 
print("All uncommon words from both the string are:",words)
