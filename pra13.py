#write a python program to find sum of natural number
start=int(input("enter start number:"))
end=int(input("enter end number"))
s=0
for i in range(start,end+1):
    s=s+i
print("sum of natural number==",s)