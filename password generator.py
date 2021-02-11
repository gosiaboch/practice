import random

list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "z"]
slowa = ["kawa", "cebula", "marchewka", "gruszka", "poduszka"]
number = random.randint(1,1000)
symbol =["_", "-", "+", "#", "@", "&", "*"]

pomieszanie = random.shuffle(list)
print(list)
wybierzLiczbe = random.choice("1234567890")

x = random.choice(list)
y = random.choice(symbol)
z = random.choice(slowa)

while True:
    wyborHasla = input("Wygenerować hasło silne czy słabe? Jeśli chcesz zakończyć wciśnij 0. Wpisz silne/słabe lub 0 : ")
    if wyborHasla == "silne":
        silneHaslo = x + y + z + wybierzLiczbe
        print(silneHaslo)
    elif wyborHasla == "słabe":
        slabeHaslo = z + wybierzLiczbe
        print(slabeHaslo)
    elif wyborHasla == 0:
        break






