a=int(input())
n=int(input())
s=0
for i in range(n):
    b,c=map(int, input().split())
    s=s+(b*c)

if a==s:
    print("Yes")
else :
    print("No")