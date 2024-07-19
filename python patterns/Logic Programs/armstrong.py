n=int(input("Enter a number to find armstrong or not:"))
s=n
length=len(str(n))
sum=0
while n!=0:
    rem=n%10
    sum+=rem**length
    n=n//10
    
if sum==s:
    print("Given {} number is armstrong number".format(s))
else:
    print("Given {} number is not armstrong number".format(s))
    