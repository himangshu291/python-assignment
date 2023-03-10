#Write a program to generating random strings until a given string is generated
import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' ., !?;:'

t=input("Enter a string:")

ch= ''.join(random.choice(possibleCharacters) for i in range(len(t)))
attemptNext = ''  
completed = False
iteration = 0
  
# Iterate while completed is false
while completed == False:
    print(ch)
    attemptNext = ''
    completed = True
      
    # Fix the index if matches with 
    # the strings to be generated
    for i in range(len(t)):
        if ch[i] != t[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += t[i]
              
    # increment the iteration 
    iteration += 1
    ch = attemptNext
    time.sleep(0.1)
  
# Driver Code
print("Target matched after " + str(iteration) + " iterations")