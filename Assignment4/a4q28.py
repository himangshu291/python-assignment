#Write a program to find consecutive characters frequency
from itertools import groupby
# initializing string
str1="hhimmmmanggshuuu"
# Consecutive characters frequency
# Using list comprehension + groupby()
res = [len(list(j)) for _, j in groupby(str1)]
 
# printing result
print("The Consecutive characters frequency : ",res)