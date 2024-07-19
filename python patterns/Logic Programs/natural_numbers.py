def natural_num(Number):
    sum=0
    for i in range(1,Number+1):
        sum+=i
    return sum
n=int(input("Enter a number :"))
print("Sum of First {} Numbers is :{}".format(n,natural_num(n)))
        
        