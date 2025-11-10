a,b=map(int,input().split())
c=int(input())

d=(a*60)+b+c
h=d//60
m=d%60

if h>=24:
    h=h%24

print(str(h) + " " + str(m))

