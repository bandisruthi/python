#hallow patterns
#square pattern:
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i ==1 or i==n or j==1 or j==n:
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#right angle triangle:
n=10
for i in range(n):
    for j in range(i+1):
        if i==j or j==0 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#num pattern  
#a.Repeat row number     
# n=5
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end=" ")
#     print()
#b.Increasing numbers in each row
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()  
#c.Continuous counting
n=5
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()    

#factorial of a num by using recursion
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
n=int(input("enter:"))
print(fact(n))