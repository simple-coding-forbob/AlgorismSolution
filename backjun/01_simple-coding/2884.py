a,b=map(int, input().split())
# 0 => 24
if a==0:
    a=24

d=(a*60)+b-45
h=d//60
m=d%60

if h>=24:
    h=h%24

print(str(h) + " " + str(m))