str1 = input(f"First Word ")
str2 = input(f"Second Word ")

def anagram_check(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    if str1 == str2 or len(str1) != len(str2):
        return False
    for char in str1:
        if str1.count(char) != str2.count(char):
            return False
    return True

print(anagram_check(str1,str2))