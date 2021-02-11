a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
c = a + b
print(c)
d = set(c)

print(d)

def deduplicate(x):
    return list(set(x))
print(deduplicate(a))
