s=0
p=0
for i in range(1,10):
    a=int(input())
    if a > s:
        s=a
        p=i

print(s)
print(p)