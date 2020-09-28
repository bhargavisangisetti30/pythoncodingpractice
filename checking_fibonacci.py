import math
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) ##gives the squareroot of given number eg:16-4,25-5
    return s*s==x
def fib(n):
     return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
n=int(input())
if (fib(n) == True): 
         print(n,"is a Fibonacci Number")
else: 
         print(n,"is a not Fibonacci Number ")
