import random
string='ABCDEFGHIJKLMNOPQRSTVWXYZ'
digit='0123456789'
spl='!@#$%&:'
m=''
for i in range(6):
    m=m+random.choice(string)
for j in range(3):
    m=m+chr(random.randint(64,100))
for k in range(2):
    m=m+random.choice(spl)

print(m)