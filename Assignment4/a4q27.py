#Write a program to word location in String
str1=input("Enter a sentence: ").split()
word=input("Enter the word whose location you want: ")
i=0
while i<len(str1):
    if str1[i]==word:
       location=i
       break
    i+=1       
print("The location of word is:",location)       
