mul = -1
res = []
num = -1
for _ in range(int(input())):
    if mul == -1:
        mul = int(input())
    else:
        num = int(input())
    if num % mul == 0 and num != -1 and mul != -1:
        res.append(num)
        mul = -1
        num = -1
for i in res:
    print(i)