num=[1,2,3,3,4,5]
d={}
for i in num:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)