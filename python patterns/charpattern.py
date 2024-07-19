n=5
alpha=ord('A')
for i in range(n):
    for j in range(n-i):
        print(" ",end=' ')
        print(" ",end=' ')
    for k in range(i):
        print(chr(alpha),end='   ')
        alpha+=1
    for m in range(i):
        alpha=65
        print(chr(alpha),end='   ')
        alpha+=1
    
    print()