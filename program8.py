#calculate working capital for company
a=float(input("Enter company-A reserved cash:"))
b=float(input("Enter company-A received cash:"))
c=float(input("Enter company-A inventories cash:"))
d=float(input("Enter company-A payable cash:"))
e=float(input("Enter company-A borrowing cash:"))
f=float(input("Enter company-A liabilites cash:"))
assets=a+c+b
liabilites=d+e+f
capital=assets-liabilites
print("********************************************************")
print("CURRENT ASSETS:",assets)
print("CURRENT LIABILITES",liabilites)
print("WORKING CAPITAL:",capital)
