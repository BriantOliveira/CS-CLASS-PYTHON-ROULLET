import random

red = (1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 30, 32, 34, 36)
black = (2, 4, 6, 8, 10, 11, 13, 15, 17, 19, 20, 22, 24, 26, 28, 29, 31, 33, 35)
green = (0, 37)



# initial amount
initial_money = 100
losses = 0

# Ask player how much is the bet


def _roulett_bet(money):
    print("How much do you want to bet?")
    bet = input(">")
    bet = int(bet)
    if bet > money:
        bet_too_much(money)
    else:
        red_or_black(bet, money, losses)
        money += int(bet)


# Prevet the user for betting much then player has


def bet_too_much(money):
    print("You are poor, get your shit together. Try again")
    input("PRESS ENTER TO CONTINUE>")
    _roulett_bet(money)

# Ask player if he wants red or black


def red_or_black(bet, money, losses):
    print("You bet {}".format(bet))
    print("Red or Black?")
    answer = input(">")
    number = random.randint(0, 37)
    if number == 1 and answer == "red":
        print("You won!")
        money += int(bet)
        print("Now you have {} money".format(money))
        print("Your losses are {}".format(losses))
        replay(money)
    elif number == 2 and answer == "black":
        print("You won!")
        money += int(bet)
        print("Now you have {} money".format(money))
        print("Your losses are {}".format(losses))
        replay(money)
    else:
        print("You lost!!!!")
        money -= int(bet)
        losses += int(bet)
        print("Now you have {} money".format(money))
        print("Your losses are {}".format(losses))
        replay(money)

    # Ask if player wants to go another round


def replay(money):
    print("do you want to play again?")
    play_again = input("YES/NO>")
    if play_again ==  "YES":
        _roulett_bet(money)
    else:
        print("Okay, bye loser!")

_roulett_bet(initial_money)
