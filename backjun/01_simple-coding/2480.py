a,b,c=map(int, input().split())

if a==b==c :
    print(10000 + a*1000)
elif a != b and b != c and a != c:
    big=max(a,b,c)
    print(big*100)
else :
    if a==b or b==c :
        print(1000+b*100)
    else :
        print(1000+a*100)

