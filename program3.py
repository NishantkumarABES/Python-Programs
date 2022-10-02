#to input itemname, selling price, cgst, sgst
item=input("enter item name:")
rate=float(input("enter GST rate on item:"))
sp=float(input("enter selling price:"))
cgst=sp*((rate/2)/100)
sgst=cgst
amount=sp+cgst+sgst
print("\tINVOICE")
print("ITEM:",item)
print("PRICE",sp)
print("CGST:",cgst)
print("SGST:",sgst)
print("amount payable:",amount)

