#find maximum of three number
def max1(num1,num2,num3):
    if num1>num2 and num2>num3:
        return num1
    elif num2>num1 and num1>num3:
        return num2
    else:
            return num3
num1=int(input("enter the number 1="))
num2=int(input("enter the number 2="))
num3=int(input("enter the number 3="))
print("the maximum of three number is=",max1(num1,num2,num3))

#output
#enter the number 1=33
#enter the number 2=63
#nter the number 3=90
#the maximum of three number is= 90

#write a program to find greatest of four number enter by user
num1=int(input("enter number 1=\n"))
num2=int(input("enter number 2\n"))
num3=int(input("enter number 3=\n"))
num4=int(input("enter number 4=\n"))


if num1>num4:
     f1=num1
else:
    f1=num4

if num2>num3:
    f2=num2
else:
    f2=num3
if f1>f2:
    print(str(f1)+"is greatest")
else:
    print(str(f2)+" is greatest")

    #output

#enter number 1=
#22
#enter number 2
#01
##enter number 3=
#76
#enter number 4=
#42
#76 is greatest