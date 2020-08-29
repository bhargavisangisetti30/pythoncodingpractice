def sum(lst):
   sum=0
   for i in lst:
     sum=sum+i
   print(sum)
lst=[]
n=int(input("no of elements:"))
for i in range(0,n):
    ele=int(input("values:"))
    lst.append(ele)
sum(lst)
