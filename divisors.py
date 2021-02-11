liczba = int(input("Proszę podać dowolną liczbę : "))

x = range(2,11)

for element in x:
    if liczba % element == 0:
        print(element)

