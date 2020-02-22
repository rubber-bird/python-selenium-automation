str = input(f"Str: ")

#str = "A6B4C4"
def uncompressing_str(compressed_str):
    result = ""
    for i in range(0, len(compressed_str) - 1, 2):
        ch = str[i]
        n = int(str[i+1])
        while n != 0:
            result += ch
            n -= 1
    return result

print(uncompressing_str(str))