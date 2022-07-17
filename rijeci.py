def fib(n,m):
    if n== 0 or n== 1:
        return n
    if n not in m:
        m[n] = fib(n- 1, m) + fib(n- 2, m)
    return m[n]
lst1 = {}
lst2 = {}
n = int(input())
print(fib(n - 1, lst1), fib(n, lst2))