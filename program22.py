#largest number

a=int(input("How many number do you want to enter:"))
largest=0
print("Enter",a,"number")
for d in range(a):
    num=int(input())
    if largest< num:
        largest=num
print("Largest number:",largest)        
    
        
