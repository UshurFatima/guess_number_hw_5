from random import choice
from decouple import config


def play(attempts, amount_left, bet):
    for i in range(attempts):
        if amount_left > 0:
            user = input("enter a number from 1 to 9: ")
            random_number = choice(config("RANGE"))
            if user == random_number:
                amount_left += bet
                bet *= 2
                print(f"user chose {user}, the number was {random_number}, "
                      f"user gained bet, amount left is {amount_left}")
            else:
                amount_left -= bet
                print(f"user chose {user}, the number was {random_number}, "
                      f"bet was lost, amount left is {amount_left}")
                if amount_left != 0 and i != 4:
                    bet = int(input("How much do you want to bet "))
        else:
            print("You don`t have enough money to continue")
            break
    print(f"The game is over. After the game the user has {amount_left}")
