#python program to print fibonacci series
num = int(input("enter limit::"))
a=0
b=1
c=0
print("fibonacci series::")
for i in range(num):
      print(c,end=" ")
      a=b
      b=c
      c=a+b

      #output:
      #enter limit::10
#fibonacci series::
#0 1 1 2 3 5 8 13 21 34