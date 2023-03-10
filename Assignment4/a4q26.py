#Write a program to convert numeric words to numbers
dict={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
str1=input("Enter numeric words:").lower().split()
str2=' '.join(dict[i] for i in str1)
print("After convert numeric words to numbers:",str2)      