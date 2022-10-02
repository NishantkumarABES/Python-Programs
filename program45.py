#wins and losses
dic={}
win=[]
loss=[]
while True:
    name=input("Enter tne name of team(Enter Q for quit):")
    if name=="Q" or name=="q":
        break
    else:
        wini=int(input("Enter the no.of wins match:"))
        lossi=int(input("Enter the no.loss match:"))
        dic[name]=[wini,lossi]
        win+=[wini]
        if wini>0:
            loss+=[name]
nam=input("Enter the name of any team(which you entered)")
print("winning percentage=",dic[nam][0]*100/(dic[nam][0]+dic[nam][1]))
print("winning list of all team=",win)
print("team who has winning records are:",loss)

        
        
