import random


def pobieranienumeru():
    while True:

        try:

            x = int(input("Guess the number: "))

            break

        except ValueError:

            print("It's not a number")
    return x


def porownanie():
    y = random.randint(1, 100)
    z = pobieranienumeru()
    while z != y:

        if z > y:
            print("To big!")

        else:
            print("to small!")

        z = pobieranienumeru()

    print("You win!")


porownanie()

