#leap year
a=int(input("Enter the year"))
if a%400==0 or (a%100!==0 and a%4==0):
    print("THE YEAR IS LEAP YEAR")
else:
    print("THE YEAR IS NOT LEAP YEAR")
    
