#calculate EMI
p=float(input("Enter principal loan amount:"))
r=float(input("Enter rate of interest per month:"))
n=float(input("Enter tenure of loan repayment in months"))
R=(r*12)/100
E=p*R*(1+R)**n/(((R+1)**n)-1)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print("PRINCIPAL LOAN AMOUNT",p)
print("RATE OF INTERSEST PER MONTH:",r)
print("ENTER TENURE OF LOAN REPAYMENT IN MONTH",n)
print("EMI",E)
