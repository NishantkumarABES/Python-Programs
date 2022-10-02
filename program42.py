#rotation of element in list
a=eval(input("Enter the list:"))

print(a)
print("_____________________________")

a.append(a[0])
a.pop(0)
print(a)
