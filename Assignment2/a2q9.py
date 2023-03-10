stk=1000
odr=int(input("Enter the customer order: "))
credit=input("Credit is ok or not: ")
if (odr<=stk and credit=='ok'):
      print("Supply has requirement.")
elif (odr<=stk and credit=='not'):
      print("Send intimation.")	
elif (stk<odr and credit=='ok'):
      print("Intimate to him data the balance will be shiped.")
else:
      print("Wrong input.")