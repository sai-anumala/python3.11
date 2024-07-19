def arm_strong(number):
    s=number
    length=len(str(number))
    sum=0
    for digit in str(number):
        sum+=int(digit)**length
    if sum==s:
        return s
    else:
        return False

print("Enter a range of number to find armstrong or not")
first_num=int(input("Enter first number:"))
last_num=int(input('Enter Last number:'))
m=[]
for i in range(first_num,last_num+1):
    if (arm_strong(i)):
        m.append(i)
print("ArmStrong numbers are :",m)