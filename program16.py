#digit to words(only for five digit number)
number=["zero","one","two","three","four","five","six","seven","eight","nine"]
n =int(input("Enter the digit:"))
if n>9999 and n<100000:
    d=[]
    while n>0:
        d.append(n%10)
        n=n//10
    print(number[d[4]],number[d[3]],number[d[2]],number[d[1]],number[d[0]]) 
else:
    print("invalid entry")
 
