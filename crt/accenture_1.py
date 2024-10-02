def conversion(n1,n2):
    n=n1*n2
    d={13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11,24:12}
    if n in d:
        return d[n]
    else:
        return n
n1=int(input('Enter 1st number:'))
n2=int(input('Enter 2nd number:'))
print(conversion(n1,n2))