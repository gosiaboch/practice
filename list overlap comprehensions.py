import random
a = random.sample(range(1,30),12)
print(a)

b = random.sample(range(1,30), 16)
print(b)

c = [i for i in a if i in b]
print(c)





