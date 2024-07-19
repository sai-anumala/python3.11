def isInside(x1,y1,x2,y2,x3,y3,x4,y4,p1,p2):
    A=(area(x1,y1,x2,y2,x3,y3)+area(x1,y1,x4,y4,x3,y3))
    A1=area(p1,p2,x1,y1,x2,y2)
    A2=area(p1,p2,x2,y2,x3,y3)
    A3=area(p1,p2,x3,y3,x4,y4)
    A4=area(p1,p2,x4,y4,x1,y1)
    if A==A1+A2+A3+A4:
        return True
    else:
        return False

def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)

input=input("Enter coordinates of Rectangle and point:")
m=input.split(",")
coordinates=[]
for i in m:
    coordinates.append(int(i))
if (isInside(*coordinates)):
    print("inside")
else:
    print("outside")
    
