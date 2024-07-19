first='ABC'
second='DEFGH'
len_a=len(first)
len_b=len(second)
result=[]
for i in range(max(len_a,len_b)):
    if i<len_a:
        result.append(first[i])
    if i<len_b:
        result.append(second[i])
result=''.join(result)
print(result)