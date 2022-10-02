#string style
print("One string should be of 6 letter")
a=input("Enter first string:")
b=input("Enter second string:")
if len(a)!=len(b):
    if len(a)>len(b):
        print("first string is bigger")
    else:
        print("second string is bigger")
    if len(a)==6:
        print(a[0],"\t\t\t",a[5])
        print("\t",a[1],"\t",a[4],"\t")
        print("\t\a\a\a",a[2],"\a",a[3],"\t\a\a\a")
    elif len(b)==6:
        print(b[0],"\t\t\t",b[5])
        print("\t",b[1],"\t",b[4],"\t")
        print("\t\a\a\a",b[2],"\a",b[3],"\t\a\a\a")    
else:
    print("Invalid entry")
