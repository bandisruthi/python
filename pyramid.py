# # Diamond       
n=5
for i in range(1,n+1):
    s="  " *(n - i)
    if i==1:
        print(s+"*")
    else:
        print(s+"* "+"  " *(2*i-3)+"*")
for i in range(n-1,0,-1):
    s="  " *(n-i)
    if i==1:
        print(s+ "* ")
    else:
        print(s +"* "+"  " *(2*i-3)+ "*")

#left-aligned half diamond
n = 5
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)

n = 5

#right-aligned half diamond 
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)
