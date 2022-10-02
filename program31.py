#modify program 30
a=1
list1=[]
list2=[]
while a<=10:
    print("item no:",a)
    b=int(input("Cost Price:"))
    list1.append(b)
    c=int(input("Selling Price:"))
    list2.append(c)
    e=c-b
    if e>0:
        print("profit of individual item:",e)
    else:
        print("loss of individual item:",e)
        a=a+1
d=sum(list1)
f=sum(list2)
g=f-d
if g>0:
    print("overall profit:",g)
else:
    print("overall loss:",g)
    
    
