n=5
alph=65
for i in range(n):
    print(" "*(n-i),end=' ')
    for j in range(i):
        print(chr(alph),end=' ')
        alph+=1
   
    alph=65
    print()