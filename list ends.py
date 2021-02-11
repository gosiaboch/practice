a = [5, 10, 15, 20, 25]

b = []

b.append(a[0])
b.append(a[-1])
print(b)

c = [5, 10, 15, 20, 25]

def listend(x):
    return [x[0], x[-1]]

print(listend(c))

mylist = "Hello"
x = len(mylist)
print(x)