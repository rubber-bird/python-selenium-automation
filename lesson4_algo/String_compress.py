str = input("")

def str_compress(string):
    counter = 1
    result = string[0]
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]
            counter += 1
        else:
            if counter > 1:
                result += str(counter)
            result += string[i+1]
            counter = 1
    if counter > 1:
        result += str(counter)
    return result

print(str_compress(str))