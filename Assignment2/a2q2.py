print("Calculate Premium")
age=int(input("Enter the age: "))
if(age<25 or age>35):
        print("Not Insured.")
sex=input("Enter Gender m For Male And f For Female: ")
loc=input("Enter the location c for city and v for village: ")
health=input("Enter the health e for excellent and p for poor: ")
if((health=='e') and (age>=25 or age<=35) and (loc=='c') and (sex=='m')):
        print("His premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.")
elif((health=='e') and (age>=25 or age<=35) and (loc=='c') and (sex=='f')):
        print("Her premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakhs.")
elif((health=='p') and (age>=25 or age<=35) and (loc=='v') and (sex=='m')):
        print("His premium is Rs. 6 per thousand and his policy amount cannot exceed Rs. 10000.")
else:
        print("Not Insured")
