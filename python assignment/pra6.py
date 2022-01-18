#python program to check armstrong number
n=int(input("enter the number= "))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if(n==sum):
    print("number is an armstrong number")
else:
    print("number is not an armstrong number")


    #output:
    #enter the number= 110
#number is not an armstrong number

#enter the number= 370
#number is an armstrong number
