a = int(input("enter the number: "))

b = []

for i in range(2, a):
    b.append(a % i)
print(b)

if 0 not in b:
    print("number is prime")

else:
    print("number is not prime")