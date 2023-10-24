a = int(input("Enter First Number :"))
b = int(input("Enter Second Number :"))
c = int(input("Enter Third Number :"))
if(a+b>c or b+c>a or a+c>b) :
    print ("We can draw triangle with these numbers :",a,b,c)
else :
    print("We can not draw triangle with these numbers : ",a,b,c)