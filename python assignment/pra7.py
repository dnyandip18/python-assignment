#python program to find factorial of number
n=int(input("enter number::"))
fac=1
for i in range (1,n+1):
    fac*=i
    print("factorial=",fac)
    
    #output
#enter number::5
#factorial= 1
#factorial= 2
#factorial= 6
#factorial= 24
#factorial= 120