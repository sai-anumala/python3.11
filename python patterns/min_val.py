inp=input("enter a list of numbers:")
l=inp.split(',')
val=l[0]
min=0
for i in range(len(l)):
    if l[i]<=val:
        min=l[i]
        
print(min)