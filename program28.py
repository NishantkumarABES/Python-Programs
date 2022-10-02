#smallest,next higher,highest
a=int(input("A=:"))
b=int(input("B=:"))
c=int(input("C=:"))
l=[a,b,c]
l.sort()

print("SMALLEST NUMBER:",l[0])
print("NEXT HIGHER NUMBER:",l[1])
print("HIGHEST NUMBER:",l[2])
