
#temperature scale
a=float(input("Enter the temprature (in celsius)"))
if a<-273.15:
    print("THE TEMPRATURE IS INVALID BECAUSE IT IS INVALID BECAUSE IT IS BELOW ABSOLUTE ZERO")
elif a==-273.15:
    print("THE TEMPRATURE IS ABSOLUTE ZERO")
elif a>-273.15 and a<0:
    print("THE TEMPRATURE IS BELOW FREEZING" )
elif a>0 and a<100 :
    print("THE TEMPRATURE IS IN THE NORMAL RANGE")
elif a==100:
    print("THE TEMPRATURE IS AT THE BOILING POINT")
elif a>100:
    print("THE TEMPRATURE IS ABOVE THE BOILING POINT")

    
    
