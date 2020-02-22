def recursive_replication(str, n):
    if n > 1:
        return recursive_replication(string, n - 1) + str
    elif n == 1:
        return str


str = input(f"String: ")
n = int(input(f"NUmber: "))
print(recursive_replication(str, n))