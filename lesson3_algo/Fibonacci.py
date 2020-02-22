def fibonacci(n):
    fibonacci_1 = 1
    fibonacci_2 = 1
    if n==0:
        print(0)
    if n > 0:
        print(fibonacci_1)
    if n > 1:
        print(fibonacci_2)
    i = 0
    while i < n-2:
        fibonacci_sum = fibonacci_1 + fibonacci_2
        fibonacci_1, fibonacci_2 = fibonacci_2, fibonacci_sum
        i += 1
        print(fibonacci_sum)

fibonacci(8)


