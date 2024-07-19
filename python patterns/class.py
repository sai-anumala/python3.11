class car:
    def __init__(self,name,age):
        self.name=name
        self.ag=age
    def display(self):
        print(self.name,self.ag)
    
c1=car('sai',21)
c1.display()