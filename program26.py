#age group
i=0
d=0
f=0
g=0
print("to end the program please enter 101")
while i==0:
    a=int(input("Enter the age group:"))
    if a==101:
        print("program is over")
    else:    
        if a>=26 and a<=35:
            d=d+1
        elif a>=36 and a<=45:
            f=f+1
        elif a>=46 and a<=55:
            g=g+1
        elif a>55 or a<26:
            print("no age group exist")
    
 
        print("no of person in age group(26-35):",d)
        print("no of person in age group(36-45):",f)
        print("no of person in age group(46-55):",g)         
          
          
    
