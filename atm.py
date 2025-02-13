class ATM:
    def __init__(self, balance=0):
        
        self.balance = balance

    def check_balance(self):
       
        print(f"Your current balance is: ₹{self.balance}")

    def deposit(self, amount):
        
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            self.check_balance() 
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
       
        if amount > self.balance:
            print("Insufficient balance. You cannot withdraw more than your current balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()

    def run(self):
        
        
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter deposit amount: ₹"))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "3":
                try:
                    amount = float(input("Enter withdrawal amount: ₹"))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break  # Exit the ATM
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":

    atm = ATM(balance=5000)
    
    atm.run()