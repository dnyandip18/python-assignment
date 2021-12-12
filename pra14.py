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