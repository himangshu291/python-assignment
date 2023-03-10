# Write a program to find all close matches of input string from a list
strings = ["Lion", "Li", "Tiger", "Tig"]
element = "Lion"
for i in strings:
   print(i.startswith(element))
   print(element.startswith(i))
   if i.startswith(element) or element.startswith(i):
      print(i, end = " ")
print()