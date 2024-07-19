n=int(input("number to convert:")) #taking input dynamically
k=bin(n) #converting into binary format
p=''.join(k)[2:] #it is used to convert from list to normal string with ignoring first 2 characters
print(p) #printing value
print(int('0101',2)) #is used to convert form binary to numerical