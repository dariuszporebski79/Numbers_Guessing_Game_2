print("Pomyśl liczbę od 0 do 1000, a ja ja zgadnę w maksymalnie 10 próbach")
min = 0
max = 1000
answer = 0
while answer != 3:
    guess = int((max-min) / 2) + min
    print("Zgaduję: ", guess)
    answer = int(input("Za dużo - wpisz 1, za mało - wpisz 2, zgadłem - wpisz 3 "))
    if answer == 3:
        print("Wygrałem :-)")
    elif answer == 1:
        max = guess
    else:
        min = guess
