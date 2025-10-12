#WAP to check string is palindrome
s="sruthi"
f=0
i=0
j=len(s)-1
while i<j:
    if s[i]==s[j]:
        i+=1
    else:
      f=1
    break
if f==1:
    print("not a palindrome")
else:
  print("palindrome")


#Nth Fibonacci number using recursion
def fibonacci(n):
    if n <= 0:
        return "Invalid input! n must be positive."
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n =7
print(f"The {n}th Fibonacci number is:", fibonacci(n))
