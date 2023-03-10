n=input("Enter Binary input numbers:")
n1=n
#temp=0
b=1
dec=0
while(n!=''):
    d=n[0]
    dgt=ord(d)-ord('0')
    #temp=temp*10+dgt        #covert string to number
    dec=dec*2+dgt
    n=n[1: ]
print(f'The decimal value of {n1} is {dec}')