def arrFib(n):
    res = []
    p = 0
    c = 1
    for i in range(n):
        res += [c]
        c, p = c + p, c
    return res


n = int(input('The element'))

arr = arrFib(1000)
print(arr[n])