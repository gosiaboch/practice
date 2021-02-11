import random

def silneHaslo():
    malaLitera = random.choices("qwertyuiopasdfghjklzxcvbnm")
    duzaLitera = random.choices("QWERTYUIOPASDFGHJKLZXCVBNM")
    symbol = random.choices("!@#$%^&*<>?,.")
    liczba = random.choices("1234567890")
    x = malaLitera + duzaLitera + symbol + liczba + liczba + malaLitera + duzaLitera + liczba + malaLitera + symbol
    random.shuffle(x)
    result = "".join(x)
    return result

def slabeHaslo():
    slowa = ["kawa", "arbuz", "podkowa", "mango", "piesek"]
    liczba = random.choices("1234567890")
    y = random.choices(slowa) + liczba
    result2 = "".join(y)
    return result2

while True:
    decyzja = int(input("Jeśli chcesz wygenerować silne hasło wciśnij 1, jeśli chcesz słabe wciśnij 2, jeśli chcesz wyjść: 0 : "))
    if decyzja == 1:
        print(silneHaslo())
    elif decyzja == 2:
        print(slabeHaslo())
    elif decyzja == 0:
        break

