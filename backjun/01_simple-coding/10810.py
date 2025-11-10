n,m=map(int, input().split())
d=[0 for _ in range(n+1)]

for _ in range(m):
    a,b,c=map(int, input().split())
    for i in range(a, b+1):
        d[i]=c

for y in range(1, len(d)):
    print(d[y],end=" ")