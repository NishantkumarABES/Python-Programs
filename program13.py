#close and not close
a=float(input("Enter the first number:"))
b=float(input("Enter the second number:"))
if a+0.001==b or a-0.001==b:
    print("CLOSE")
else:
    print("NOT CLOSE")
