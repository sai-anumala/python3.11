def str2num(num):
    d={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    sum=0
    for i in num:
        if i in d:
            sum=sum*10+d[i]
    return sum+1
n=input("enter a string:")
print(n)
print(str2num(n))
