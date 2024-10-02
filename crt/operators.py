n=input("Enter a input:")
i=1
a=int(n[0])
while i<len(n):
    if n[i]=='A' or n[i]=='a':
        a=a&int(n[i+1])
    elif n[i]=='B' or n[i]=='b':
        a=a|int(n[i+1])
    elif n[i]=='C' or n[i]=='c':
        a=a^int(n[i+1])
    i=i+1
    
print(a)
        