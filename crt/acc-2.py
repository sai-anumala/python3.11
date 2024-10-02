def sumofmultiples(n,li):
    cnt=0
    for i in range(n-1):
        for j in range(i+1,n):
            if (li[i]*li[j])%3==0:
                cnt+=1
    return cnt

n=int(input())
li=list(map(int,input().split()))
print(sumofmultiples(n,li))