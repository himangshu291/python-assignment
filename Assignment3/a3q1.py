s=0
for i in range(10):
    n=int(input(f"Overtime of employee {i+1}: "))
    pay=n*12.00
    s=s+pay
print("Total overtime pay of 10 employees:",s)
