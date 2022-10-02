#first odd number
a=int(input("Enter the number(odd):"))
if a%2==1:
    while a>0:
        print("-->",a)
        a=a-2
    print("LOOP IS OVER")
else:
    print("invalid entry")
    
