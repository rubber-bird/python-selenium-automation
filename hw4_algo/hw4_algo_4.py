z = int(input('Osnova: '))
c = int(input('Pokaznyk: '))

def stepin(a, b):
    if b == 0 or b < 0:
        return 1
    else:
        return a * stepin(a, b - 1)

print(stepin(z, c))
