#divisible and (even odd)
a=int(input("Enter the last number"))
b=int(input("Enter the dividend"))
for e in range(1,a+1):
    if e%b==0:
        print(e,"divisible by",e)
        if e%2==0:
            print(e, "number is even")
        else:
            print(e,"number is odd")
    else:
        print(e)
        
    

      
