#triangle or not
a=float(input("Enter the length of first side:"))
b=float(input("Enter the length of second side:"))
c=float(input("Enter the length of third side:"))
if a+b>c and b+c>a and c+a>b:
    print("IT IS THE TRIANGLE")
else:
    print("IT IS NOT THE TRIANGLE")
