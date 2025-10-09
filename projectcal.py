class calculator:
   def __init__(self,name):
     self.name=name
     
   def addition(self,a,b):
      return a+b
   def substraction(self,a,b):
      return a-b
   def multiplication(self,a,b):
      return a*b
   def division(self,a,b):
      return a/b
   def reminder(self,a,b):
      return a%b   
print("types of operations")
print("1.addition \n 2.substration \n 3.multiplication \n 4.division \n 5.reminder \n 6.exit \n 7.name")
name=input("enter your name")
cal1=calculator(name)
while True:
    n=int(input("enter option: "))
    if n==1:
        a,b=map(int,input("enter value: ").split())
        print(cal1.addition(a,b))
    elif n==2:
        a,b=map(int,input("enter value: ").split())
        print(cal1.substraction(a,b))
    elif n==3:
        a,b=map(int,input("enter value: ").split())
        print(cal1.multiplication(a,b))
    elif n==4:
        a,b=map(int,input("enter value: ").split())
        print(cal1.division(a,b))
    elif n==5:
        a,b=map(int,input("enter value: ").split())
        print(cal1.reminder(a,b))
    elif n==6:
        break
    elif n==7:
      print(cal1.name)
    else:
        print("please enter a valid option") 