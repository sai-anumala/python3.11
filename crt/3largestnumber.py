def large(num):
    n=len(num)
    a=''
    for i in range(n):
        if i+2<n and num[i]==num[i+1] and num[i]==num[i+2]:
            a=max(a,num[i:i+3])
        return a
n=[1,22,66,7,4,4,4,8]