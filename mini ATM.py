PIN = int(input("Enter your PIN : "))
print("-------------------------------------------------------------")

balance = 10000

if PIN == 8675:

    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Total Balance")
        print("4. Exit")
        print("-------------------------------------------------------------")

        choice = int(input("Enter your choice : "))
        print("-------------------------------------------------------------")

        if choice == 1:
            deposit = int(input("Enter your Amount : "))
            balance = balance + deposit
            print("Balance :", balance)

        elif choice == 2:
            withdraw = int(input("Enter your Amount : "))

            if withdraw <= balance:
                balance = balance - withdraw
                print("Balance :", balance)
            else:
                print("Invalid Amount")

        elif choice == 3:
            print("Total Balance :", balance)

        elif choice == 4:
            print("Thank you!")
            break

        else:
            print("Invalid choice")

        print("-------------------------------------------------------------")

else:
    print("Invalid PIN")


        
        
