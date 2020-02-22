str = input("str: ")
ch = input("ch: ")

def duplicate_search(str, ch):
    counter = 0
    for i in str:
        if i == ch:
            counter += 1
    return counter


print(duplicate_search(str, ch))