from datetime import datetime

print("\n==== Welcome to the secure ATM Banking System ====\n")


def record_transaction(transaction_type, amount, balance, status):
    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the history record
    record = f"{timestamp} | {transaction_type} | Amount: {amount} | Balance: {balance} | Status: {status}\n"

    # Open file in append mode and write the record
    with open("detail.txt", "a") as file:
        file.write(record)

balance = 3500

def display_balance():
    print("Your Total Balance is: ", balance)

def deposit():
    global balance
    try:
        amount = int(input("Enter the amount you want to add: "))
        if amount <= 0:
            print("Invalid Amount. Try Again")
            record_transaction("Deposit", amount, balance, status = "Failed")
            return
    except ValueError:
        print("Enter a valid numerical value.")
        record_transaction("Withdrawal", amount, balance, status = "Failed")
        return
    else:
        balance += amount
        print("Successful Transaction.\n")
        record_transaction("Deposit", amount, balance, status = "Success")


def withdraw():
    global balance
    try:
        amount = int(input("Enter the amount you want to withdraw: "))
        if amount <= 0 or amount > balance:
            print("Invalid Amount. Try Again")
            record_transaction("Withdrawal", amount, balance, status = "Failed")
            return
    except ValueError:
        print("Enter a valid numerical value.")
        record_transaction("Withdrawal", amount, balance, status = "Failed")
        return
    else:
        balance -= amount
        print("Successful Transaction.\n")
        record_transaction("Withdrawal", amount, balance, status = "Success")


def show_history():
    try:
        with open("detail.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("File does not exist")


while True:
    print("--------------- OPTIONS ---------------\n1. Balance\n2. Deposit\n3. Withdrawal\n4. Transaction History\n5. Exit")
    try:
        option = int(input("Enter your desired option: "))
    except ValueError:
        print("Enter a valid numerical option.")
    else:
        if option == 1:
            display_balance() 
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 4:
            show_history()
        elif option == 5:
            break
        else:
            print("Invalid option.")