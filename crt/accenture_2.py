def unique_pair_sum(n1, n2):
    cnt = 0
    for i in range(n1-1):
        if (n2[i]*n2[i+1])%3==0:
            print(n2[i],n2[i+1])
            cnt=cnt+1
    return cnt

n1 = int(input())
n2 = list(map(int, input().split(",")))
print(unique_pair_sum(n1, n2))
