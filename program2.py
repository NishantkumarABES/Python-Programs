s="words and 987"
a=""
for i in s:
    if i.isnumeric():
        a=a+i
    else:
        if i=="-":
            a=a+"-"
        else:
            pass
print(int(a))
        


