n = int(input('Enter number'))

def to_bin(n):
    bin_string = ''
    while n>0:
        bin_string += str(n % 2)
        n = n // 2
        return int(bin_string[::-1])

def binary_gap(n):
    n = to_bin(n)
    max_gap = 0
    counter = 0

    for item in n:
        if item == '1':
            if max_gap < counter:
                max_gap = counter
            counter = 0
        else:
            counter += 1


    print(max_gap)
print(to_bin(n))