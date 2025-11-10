a=int(input())
n=map(int, input().split())

b= -1000000
s=1000000
for i in n:
   if(i > b):
       b=i
   if(i< s):
       s=i
print(str(s) + " " + str(b))