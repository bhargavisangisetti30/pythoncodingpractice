def xyz(n):
    x=0
    for i in range(1,(n//2+1)):
        if n%i==0:
            print(i,end=" ")
            x+=i
    if(x==n):
      print("yes")
    else:
      print("no")

n=int(input("num:"))
xyz(n)


##def xyz(n):
##  return n == sum([i  for i in range(1,n//2+1)])
##print(xyz(int(input())))
