class calculator:
    print("select your option")
    print("1.Addition /n 2.Subtraction /n 3.Multiplication /n 4.Division /n 5.Remainder /n 6.name /n 7.Exit")
    def __init__(self,name):
        self.name=name
    def add(self,a,b):
            return a+b
    def sub(self,a,b):
            return a-b
    def mul(self,a,b):
            return a*b
    def div(self,a,b):
            return a/b
    def rem(self,a,b):
            return a%b
name=input("enter your name")
c1=calculator(name)
while True:
    n=int(input("select:"))
    if n==1:
           a,b=map(int,input("enter a data:").split())
           print(c1.add(a,b))
    if n==2:
           a,b=map(int,input("enter a data:").split())
           print(c1.sub(a,b))
    if n==3:
           a,b=map(int,input("enter a data:").split())
           print(c1.mul(a,b))
    if n==4:
           a,b=map(int,input("enter a data:").split())
           print(c1.div(a,b))          
    if n==5:
           a,b=map(int,input("enter a data:").split())
           print(c1.rem(a,b))
    if n==6:
           print(c1.name)
    if n==7:
           break
          
        
        
