#python program to check prime number
num=int(input("enter number::"))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print("is not a prime number",num)
            break
        else:
            print("number is prime",num)
else:
            print("number is not prime",num)

            #output
#enter number::18
#is not a prime number 18

#enter number::7
#number is prime 7