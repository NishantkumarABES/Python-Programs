 #cost price and selling price 
a=1
list1=[]
list2=[]
while a<=10:
    print("item no:",a)
    b=int(input("Cost Price:"))
    list1.append(b)
    c=int(input("Selling Price:"))
    list2.append(c)
    a=a+1
d=sum(list1)
f=sum(list2)
g=f-d
if g>0:
    print("profit:",g)
else:
    print("loss:",g)
    
    

          
    
          
    
    
   
