#geater than 10
print("Enter the list containing numbers between 1 and 12")
a=eval(input("Enter list:"))
b=len(a)
print(a)
for d in range(0,b):
    if a[d]>12:
        print("Invalid Entry")
    else:
         if a[d]>=10 and a[d]<=12:
            a[d]=10
         else:
           a[d]=a[d]
print(a)        
