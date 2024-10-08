#Right-Angled Triangle without inner-spaces
n=5
for i in range(n):
    print('* '*i)
    
#Right_angled triangle with inner-space
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')

        
    
#Left-angled Triangle without inner-spaces
n=5
for i in range(n):
    print(" "*(n-i)+'*'*i)
    
#left angled triangle with inner spaces
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print(' '*(n-i)+'*'*i)
    else:
        print(' '*(n-i)+'*'+' '*(i-2)+'*')

#Equilateral Triangle without spaces
n=5
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1)) #Here 2*i-1(odd) used to print no.of stars
    
#Equilateral Triangle with spaces
n=5
for i in range(1,n+1):
    if i==1 or i==n:
        print(' '* (n-i)+'*'*(2 * i - 1))
    else:
        print(' '* (n-i)+'*'+ ' ' * (2 * i - 3)+'*') 

#Inverted Right-Angled Triangle without inner spaces
n=5
for i in range(n,0,-1):
    print('*'*i)
    
#Inverted Right-Angled Triangle with inner spaces
n=5
for i in range(n,0,-1):
    if i==n or i==1:
        print('*'*i)
    else:
        print('*'+' '*(i-2)+'*')
        
#Inverted Left-Angled Triangle without inner spaces
n=5
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*i)
    
#Inverted Left-Angled Triangle with inner spaces
n=5
for i in range(n,0,-1):
    if i==n or i==1:
        print(' '*(n-i)+'*'*i)
    else:
        print(' '*(n-i)+'*'+' '*(i-2)+'*')
        
#Inverted Eq.triangle without inner spaces
n=5
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))
    
#Inverted Eq.triangle with inner spaces
n=5
for i in range(n,0,-1):
    if i==n or i==1:
        print(' '*(n-i)+'*'*(2*i-1))
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
        
#Diamond without inner spaces
n=5
for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1,0,-1):
    print(' '*(n-i)+'*'*(2*i-1))
    
#Diamond with inner spaces
n=5
for i in range(1,n+1):
    if i==1:
        print(' '*(n-i)+'*')
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')
for i in range(n-1,0,-1):
    if i==1:
        print(' '*(n-i)+'*')
    else:
        print(' '*(n-i)+'*'+' '*(2*i-3)+'*')

#Pascal's Triangle
n=5
for i in range(n+1):
    print(' '*(n-i),end='')
    val=1
    for j in range(i+1):
        print(val,end=' ')
        val=val*(i-j)//(j+1)   #to get next value
    print()
