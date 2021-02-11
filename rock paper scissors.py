k = "kamień"
p = "papier"
n = "nożyce"


while True:
    player1 = input("Proszę wybrać kamień, papier lub nożyce : ")
    player2 = input("Proszę wybrać kamień, papier lub nożyce : ")

    if player1 == player2:
        print("Remis")
    elif player1 == k and player2 == p:
        print("Wygrywa player2!")
    elif player1 == k and player2 == n:
        print("Wygrywa player1!")
    elif player1 == p and player2 == k:
        print("Wygrywa player1!")
    elif player1 == p and player2 == n:
        print("Wygrywa player2!")
    elif player1 == n and player2 == k:
        print("Wygrywa player2!")
    elif player1 == n and player2 == p:
        print("Wygrywa player1!")
    else:
        print("Błąd")
        break












