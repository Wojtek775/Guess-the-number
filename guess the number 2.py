def wybór():
    x = ["za dużo", "za mało", "zgadłeś"]

    while True:
        odpowiedz = input("napisz czy za dużo czy za mało czy zgadłem")
        if odpowiedz in x:
            break
        print("wprowadź odpowiednią wartość : za dużo,za mało,zgadłeś")
    odpowiedz = str(odpowiedz)
    return odpowiedz


def gra():
    print("pomyśl liczbę od 0 do 1000 a ja zgadne w max 10 próbach")
    min = 0
    max = 1000
    odpowiedz = ""  # czemu to tu musi być ?

    while odpowiedz != "zgadłeś":
        guess = int((max - min) / 2) + min
        print(f"Zgaduję : {guess}")
        odpowiedz = wybór()
        if odpowiedz == "za dużo":
            max = guess
        elif odpowiedz == "za mało":
            min = guess
    print("wygrałem")


gra()
