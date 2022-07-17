input()
string = input()
res = []
a = ['ABC',3, 0]
b = ['BABC',4, 0]
c = ['CCAABB',6, 0]
for i, n in enumerate(string):
    if n == a[0][i % a[1]]:
        a[2] +=1
    if n == b[0][i % b[1]]:
        b[2] +=1
    if n == c[0][i % c[1]]:
        c[2] +=1
res = [max([a[2],b[2],c[2]])]
if a[2] == res[0]:
    res.append('Adrian')
if b[2] == res[0]:
    res.append('Bruno')
if c[2] == res[0]:
    res.append('Goran')
for i in res:
    print(i)