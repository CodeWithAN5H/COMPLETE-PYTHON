# PYTHON BANKING PROGRAM

def show_balance(balance):
    print(f"************************")
    print(f"Your balance is: ${balance:.2f}")
    print(f"************************")

def deposit(balance):
    print(f"************************")
    amount = float(input("Enter the amount you want to deposit: "))
    print(f"************************")
    if amount < 0:
        print("The amount cannot be negative.")
        return 0
    else:
        return amount

def withdraw(balance):
    print(f"************************")
    amount = float(input("Enter the amount you want to withdraw: "))
    print(f"************************")
    if amount > balance:
        print("Insufficient funds.")
        return 0
    elif amount < 0:
        print("The amount cannot be negative.")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("BANKING PROGRAM")
        print("************************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            show_balance(balance)
        elif choice == 2:
            balance+= deposit(balance)
        elif choice == 3:
            balance -= withdraw(balance)
        elif choice == 4:
            is_running = False
        else:
            print("Invalid choice")

    print("THANK YOU HAVE A NICE DAY!")

if __name__ == "__main__":
    main()