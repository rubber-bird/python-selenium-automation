n = int(input('Number'))
result = 1

if n<0:
    print('You want to get gamma function?')
elif n == 0:
    print(result)
else:
    for i int ranget(1, n+1):
        result *= i

print(result)