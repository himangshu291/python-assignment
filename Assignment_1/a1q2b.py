'''print("Calculate aggregate marks--")
marks=[]
n=int(input("Enter the no. of subjects:"))
print("Enter the marks:")
for i in range(0,n):
    ele=int(input())
    marks.append(ele)           #append is used to store the element into an array 
total=0
for i in range(0,n):
    total+=marks[i]
aggregate=total//n
percent=(total/(100*n))*100
print("Aggregate of the marks:",aggregate)
print("Percentage of the marks:"
      ,percent,"%")


'''
maths=float(input("Enter marks for maths: "));
computerscience=float(input("Enter marks for computerscience: "));
physics=float(input("Enter marks for physics: "));
chemistry=float(input("Enter marks for chemistry: "));
biology=float(input("Enter marks for biology: "));
aggtmarks=(maths+computerscience+physics+chemistry+biology)/5
percentage=((maths+computerscience+physics+chemistry+biology)/500)*100
print("Aggregate marks obtained by student: ",aggtmarks)
print("Percentage obtained by student: ",percentage)
