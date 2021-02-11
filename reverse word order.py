string = input("Proszę wpisać wybrane zdanie: ")
result = string.split()

def reverse(x):
    x = result[::-1]
    return x

print(reverse(result))

newstring = " ".join(reverse(result))
print(newstring)





