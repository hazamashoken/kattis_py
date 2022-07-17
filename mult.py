from re import L


mul = 1
res = []
num = 0
for _ in range(int(input())):
    if mul == 1:
        mul = int(input())
    else:
        num = int(input())
    print(mul,num)
    if num % mul == 0:
        res.append(num)
        mul = 1
for i in res:
    print(i)