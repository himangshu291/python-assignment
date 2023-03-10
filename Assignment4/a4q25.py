#Write a program to print permutation of a given string using inbuilt function
from itertools import permutations
def allPermutations(str):
   permList = permutations(str)
   for i in list(permList):
        print (''.join(i))
str = input("Enter a string: ")
allPermutations(str)    



'''from itertools import permutations
import string
 
s = input("Enter a string: ")
a = string.ascii_letters
p = permutations(s)
 
# Create a dictionary
d = []
for i in list(p):
 
    # Print only if not in dictionary
    if (i not in d):
        d.append(i)
        print(''.join(i))   
'''        