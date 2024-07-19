for i in range(7):
    for j in range(7):
        if i==0 and j==3 or i==1 and j==2 or i==1 and j==2 and j==4 or i==2 and j==5 or i==3 and j>=0 and j<=6:
            print("* ",end='')
        else:
            print(" ",end='')
    print()