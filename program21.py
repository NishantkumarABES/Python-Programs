#tipsy topsy
a=int(input("Enter a number(N>20):"))
if a>20:
    for b in range(11,a+1):
        if b%3==0 and b%7==0:
            print("tipsy topsy")
        elif b%7==0:
            print("topsy")
        elif b%3==0:
            print("tipsy ")
        else:
            print(b)
else:
    print("Invalid entry")
    
