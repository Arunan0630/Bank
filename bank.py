balance=5000
user_name = input("Enter your name :")
password = input("Enter password :")
if user_name == "Arun" and password =="1234":
    print("Login successfull")
    print("Select option")
    option=input("Creat account /Check Balance/Withdraw Money /Deposit Money /Exit :")

    if option == "Check Balance":
        print(balance)

    elif option == "Withdraw Money":
       amount_1=int(input("Enter your withdraw amount: "))
       if amount_1 <= balance :
           balance = balance-amount_1
           print("it is your new balance :",balance)
           print("it is your withdraw amount :",amount_1)
           
       else:
            print("check your withdraw amount, it is greater than your balance")

    elif option == "Deposit money":
        amount_2 = int(input("enter your deposit amount :"))
        if amount_2 > 0 :
            balance = balance + amount_2
            print("it is your new balance :",balance)
            print("it is your deposit amount :",amount_2)

        else:
            print("check your deposit amount, it is lower than 0 ")

    elif option =="exit":
        pass






        