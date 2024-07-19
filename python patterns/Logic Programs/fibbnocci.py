def fib(number):
    a,b=0,1
    series=[]
    while len(series)<n:
        series.append(a)
        a,b=b,a+b
    return series

n=int(input('Enter a series of fibbonacci :'))
print("Fibbonacci series is :",fib(n))
    
    
    