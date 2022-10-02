#add elements of two lists
l=eval(input("Enter list-L:"))
m=eval(input("Enter list-M:"))
a=len(l)
list=[]
if len(l)==len(m):
    for f in range(0,a):
        o=l[f]+m[f]
        list.append(o)
else:
    print("Invalid Entry")
print("Resultant list:")
print(list)

