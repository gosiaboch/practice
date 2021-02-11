a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c =[]

for x in b:
    if x in a:
        print(x)
        c.append(x)
print(c)

d = [1, 2, 3]
e = [5, 10, 15]
wszystkieLiczbymnozone = [m*n for m in d for n in e]
print(wszystkieLiczbymnozone)

f = [i for i in a if i in b]
print(f)





