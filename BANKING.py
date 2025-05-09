print("====== Welcome to Banking ======")
print("Create account: select 1 :")
print("login account: select 2:")
start = input(":")

# ========================= create account ===================================================
import random

def create_account():
    account_num = random.randint(1,100) 
    
    balance = int(input("enter your balance: "))
    name = input("enter your name: ")
    password = input("enter your password: ")

    with open("accounts.txt", "a") as file:
        file.write(f"{account_num},{name},{password},{balance}\n")

    print(f"acount_num is {account_num} your account saved succsesfully!")


# ========================= load account =========================================
def load_accounts():
    accounts = {}
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
               
                if len(parts) == 4:
                    account_num, name, password, balance = parts
                    accounts[name] = {"password": password, "balance": int(balance)}
               
                else:
                    print("Skipping malformed line:", line.strip())
    
    except :
        print("Accounts file not found!")
    
    return accounts
# ========================= save account ====================================
def save_new_updates(accounts):
    with open("accounts.txt", "w") as file:
        for name, data in accounts.items():
            file.write(f"68,{name},{data['password']},{data['balance']}\n")

# ========================= withdraw =============================================
def withdraw(accounts, user_name):
    amount = int(input("Enter your withdraw amount: "))

    if amount <= accounts[user_name]["balance"]:
        accounts[user_name]["balance"] -= amount
        print("Transaction successful!")
        print("Your new balance is:", accounts[user_name]["balance"])
        save_new_updates(accounts)
    
    else:
        print(" Please check the amount.")

# ========================= deposit ==============================================================
def deposit(accounts, user_name):
    amount = int(input("Enter your deposit amount: "))

    if amount > 0:
        accounts[user_name]["balance"] += amount
        print("Deposit successful!")
        print("Your new balance is:", accounts[user_name]["balance"])
        save_new_updates(accounts)
    
    else:
        print("Invalid deposit amount!")

# ========================= code for app ==============================================
if start == "1":
   create_account()

elif start == "2":
    accounts = load_accounts()
    print("(((φ(◎ロ◎;)φ)))")
    user_name = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_name in accounts and accounts[user_name]["password"] == password:
        print("Login successful!")
        while True:
            print("===============Select an option======================\n"
                           "Check Balance (c)\n"
                           "\n"
                           "Withdraw Money (w)\n"
                           "\n"
                           "Deposit Money (d)\n"
                           "\n"
                           "Exit (e): ")
            option=input(":")
            
            if option == "c":
                print("Your balance is:", accounts[user_name]["balance"])
            
            elif option == "w":
                print("")
                withdraw(accounts, user_name)
            
            elif option == "d":
                deposit(accounts, user_name)
            
            elif option == "e":
                print("Thank you for use banking!")
                break
            
            else:
                print("Invalid option. Please try again.")
    
    else:
        print("Invalid username or password!")

else:
    print("Please select a correct option!")

