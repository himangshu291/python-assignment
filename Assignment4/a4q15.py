#Write a program to specific Characters Frequency in String List
# Frequency of each character in string

# Get string from user
string = input("Enter some text: ")

# Set frequency as empty dictionary
frequency_dict = {}
for i in string:
    if i in frequency_dict:
        frequency_dict[i] += 1
    else:
        frequency_dict[i] = 1

print("\n--------------------------")
print("Character\tFrequency")
print("--------------------------")
for i, frequency in frequency_dict.items():
    print(i, frequency)