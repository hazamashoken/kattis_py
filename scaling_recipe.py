n,x,y = map(int, input().split())
res = []
for _ in range(n):
    res.append(int(input())/x*y)
for i in res:
    print(int(i))