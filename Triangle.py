import math

a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
if(a+b>c and b+c>a and a+c>b) :
    print ("We can draw triangle with these numbers :",a,b,c)
else :
    print("We can not draw triangle with these numbers : ",a,b,c)
