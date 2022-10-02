#reverse
w=int(input("Enter the number of item in list:"))
list=[]
for a in range(1,w+1):
    u=int(input())
    list.append(u)
print(list)
list.reverse()
print("reverse of entered list")
print(list)
