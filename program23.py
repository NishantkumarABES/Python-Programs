#second largest
list=[]
a=int(input("How many digits do you want to enter:"))
print("Enter",a,"number")
for f in range(a):
    temp=int(input())
    list.append(temp)
list.sort()
print(list)
print("second largest:",list[-2])    
    
       
