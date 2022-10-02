#seven day temperature
import pandas as pd
a=7
j=1
list=[]
list2=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

while j<=a:
    n=j-1
    print(list2[n])
    o=int(input("Temperature-"))
    list.append(o)
    j=j+1
q=pd.Series(list,index=list2)
print("-------------------------------")
print("tempreature of seven days")
print(q)
