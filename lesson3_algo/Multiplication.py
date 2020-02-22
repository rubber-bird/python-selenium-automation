def multiplication(num1, num2):
    iterator = 0
    result = 0
    while iterator < num2:
        result += num1
        iterator += 1

    return result

print(multiplication(6,6))