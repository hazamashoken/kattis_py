lst = []
ln = int(input())
def score(lt):
    res = 0
    for i,n in enumerate(lt):
        res += (1/5.0) * n * (4/5) ** (i)
    return res
for _ in range(ln):
    lst.append(int(input()))
print(score(lst))
print(sum(score(lst[:i]+lst[i+1:]) for i in range(ln))/ln)