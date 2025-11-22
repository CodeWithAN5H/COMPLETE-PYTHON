# PYTHON Slot Machine
import random


def spin_row():
    row = ['🍒','🍉','🍋','🔔','⭐']
    return [random.choice(row) for _ in range(3)]

def print_row(row):
    print("==============")
    print(" | ".join(row))
    print("==============")

def get_payout(bet, row):
    payout = 0
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            payout = bet * 3
        elif row[0] == '🍉':
            payout = bet * 4
        elif row[0] == '🍋':
            payout = bet * 5
        elif row[0] == '🔔':
            payout = bet * 10
        elif row[0] == '⭐':
            payout = bet * 20
    return payout

def main():
    print("------------------------")
    print("Symbols: 🍒🍉🍋🔔⭐")
    print("------------------------")
    balance = 100

    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Enter your bet: ")
        if not bet.isdigit():
            print("Enter a valid number")
            continue

        bet = int(bet)

        if bet > balance:
            print("You don't have enough balance")
            continue

        elif bet <= 0:
            print("Bet can't be zero or negative")
            continue

        balance -= bet

        row = spin_row()
        print_row(row)

        payout = get_payout(bet, row)

        if payout > 0:
            print(f"You Won, you got ${payout}")
        else:
            print(f"You Lost")
        balance += payout

        if balance > 0:
            if input("Do you want to play again? (Y/N): ").upper() == "N" :
                print("Thank you for playing")
                print(f"Your final balance: ${balance}")
                break

if __name__ == '__main__':
    main()