str1 = input("Str: ")
str2 = input("Old Substr: ")
str3 = input("New Substr: ")

# str1 = 'helloasd'
# str2 = 'asd'
# str3 = 'dsa'

def strch(str, substr, newsubstr):
    i = 0
    result = ''
    temp = ''
    for c in str:
        if c == substr[i]:
            i += 1
            temp += c
        else:
            i = 0
            if temp:
                result += temp
                temp = ''
            result += c

        if len(temp) == len(substr):
            result += newsubstr
            temp = ''
            i = 0
    else:
        if temp:
            result += temp

    return result

print(strch(str1, str2, str3))

