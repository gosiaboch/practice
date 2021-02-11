import random

wylosowanaLiczba = random.randint(1, 9)
print(wylosowanaLiczba)

while True:
    dzialanie = int(input("Proszę wybrać liczbę od 1 do 9 : "))
    if dzialanie == wylosowanaLiczba:
        print("Gratulację! Udało Ci się odgadnąć liczbę!")
        break
    elif dzialanie > wylosowanaLiczba:
        print("Liczba, której szukasz jest mniejsza")
    elif dzialanie < wylosowanaLiczba:
        print("Liczba, której szukasz jest większa")
