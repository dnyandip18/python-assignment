#python program to find factorial of number
n=int(input("enter number::"))
fac=1
while(n>0):
    fac=fac*n
    n=n-1
    print("factorial=",fac)
    