sticks = 21
print ("There are 21 matchsticks, you can take 1-4 number of sticks at a time.")
print ("Whoever is forced to pick up the last matchstick loses the game")
while True:
    print("Sticks left= ",sticks)
    print()
    p=int(input("Pick one sticks between 1 to 4: "))
    if(p<1 or p>4):
        print("Sorry wrong choice..")
        continue
    if(sticks==1):
        print("You took the last stick, You loose")
        break
    print("Computer picks: ",5-p)
    sticks-=5
