#simple interest calculator
a=float(input("Enter principal amount:"))
b=float(input("Enter rate:"))
c=int(input("Enter time:"))
si=a*b*c/100
x=si+a
print("_______________________________________")
print("PRINCIPAL AMOUNT:",a)
print("RATE:",b,"%")
print("TIME:",c,"year")
print("SIMPLE INTEREST:",si)
print("TOTAL PAYABLE AMOUNT:",x)        
