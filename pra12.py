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