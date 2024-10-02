def unique_pairs_sum(n1,n2):
    t=[]
    k=[]
    cnt=0
    for i in range(n1-1): #size=3-1 goes to 1
        for j in range(i+1,n1): #size=3 goest to 2
            t.append((n2[i],n2[j]))
    tuple(t)
    for i in list(t):
        k.append(list(i))
    for j in k:
        if (j[0]*j[1])%3==0:
            cnt+=1
    return cnt
  

n1=int(input())
n2=list(map(int,input().split(',')))    
print(unique_pairs_sum(n1,n2))  