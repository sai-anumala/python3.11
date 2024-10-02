def difference(n,m,a1,a2):
    max1=max(a1)
    max2=max(a2)
    min1=min(a1)
    min2=min(a2)
    return(max(abs(max1-min2),abs(max2-min1)))



n,m=map(int,input().split())
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
print(difference(n,m,a1,a2))
