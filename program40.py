n=int(input())
for i in range(n):
     for j in range(1+i,n+1):
          print(2*j-1,end=" ")
     for k in range(1,1+i):
          print(2*k-1,end=" ")
     print("")
