def creat_account():
    name= input("Enter your name:")
    balance= float(input("Enter initial balance:"))
    if balance < 0:
        print("balance must be zero or more.")
        return
    account_number = str(len(account)+1)
    accounts[account_number] ={
        "name":name,
        "balance":balance,
        "transactions":[f"account created with balance {balance}"]
    }
    print(f"account created. Your account number is {account_number}")

def deposit():
    acc = input("Enter account number :")
    if acc not in accounts :
        print("Account not found.")
        return
    amount = float(input("Enter amount to deposit:"))
    if amount <= 0:
        print("Amount must be positive.")
        return
    accounts[acc]["balance"] += amount
    accounts[acc]["transactions"]. append(f"Deposited{amount}")
    print("Deposit successfull.")
def withdraw():
    acc = input("Enter account number:")
    if acc not in accounts :
        print("Account not found.")
        return
    amount = float(input("Enter amount to withdraw"))
    if amount <= 0 or amount > accounts[acc]["Balance"]:
        print("Invalid amount")
        return
    accounts[acc]["balance"] -= amount
    accounts[acc]["transactions"].append(f"withdrew {amount}")
    print("withdrawal successful.")

def check_balance() :
    acc = input("Enter account number:")
    if acc in accounts:
        print(f"your balance is: {accounts[acc]['balance']}")
    else:
        print("Account not found.")

   

    

