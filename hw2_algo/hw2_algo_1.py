number = int(input('Enter number'))

sum = 0

while number > 0:
    a = number % 10
    number = number // 10
    sum += a

print(sum)
