def code(n):
    if n==0 or n==1:
        return n
    else:
        return n*code(n-1)

n=int(input("Enter a number:"))
print("result is",code(n))
