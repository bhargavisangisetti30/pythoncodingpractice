def mul(lst):
   mul=1
   for i in lst:
     mul=mul*i
     print(mul)
lst=[]
n=int(input("no of elements:"))
for i in range(0,n):
    ele=int(input("values:"))
    lst.append(ele)
mul(lst)
