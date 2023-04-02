print("Pomyśl liczbę od 0 do 1000, a ja ja zgadnę w maksymalnie 10 próbach")
min = 0
max = 1000
answer = 0
while answer != "zgadłeś":
    guess = int((max-min) / 2) + min
    print("Zgaduję :-) ;-): ", guess)
    while True:
        answer = input("Wpisz \"za dużo\" lub \"za mało\" lub \"zgadłeś\" :-) ")
        if answer == "zgadłeś":
            print("Wygrałem :-)")
            break
        elif answer == "za dużo":
            max = guess
            break
        elif answer == "za mało":
            min = guess
            break
        else:
            print("Pomyliłeś się lub oszukujesz ;-)")
