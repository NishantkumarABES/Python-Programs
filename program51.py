#seven day temperatuer
import pandas as pd
a=7
j=1
list=[]
list2=[1,2,3,4,5,6,7]
while j<=a:
    print("Day-",j)
    o=int(input("Temperature-"))
    list.append(o)
    j=j+1
q=pd.Series(list,index=list2)
print("-------------------------------")
print("tempreature of seven days")
print(q)
