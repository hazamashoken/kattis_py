res = 0
bal = 0
for _ in range(int(input())):
    num = int(input())
    bal += num
    if bal < 0:
        res -= bal
        bal = 0
print(res)