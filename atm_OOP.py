# pascal case
# HelloWorld

class AtmMachine:
    def __init__ (self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(
            """
            Hi how can i help you?

            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balence
            4. Press 4 to withdraw
            5. AnythingAny other character to exit
            """
        )
    
        if user_input == "1":
            #create a pin
            self.create_pin()

        elif user_input == "2":
            # change pin
            self.change_pin()

        elif user_input == "3":
            #check balance
            self.check_balance()

        elif user_input == "4":
            # withdraw
            self.withdraw_balance()
        
        else:
            exit()
    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.balance - user_balance

        print("Pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new pin: ")
            self.pin = new_pin
            print("Pin changed successfully!")
            self.menu()
        else:
            print("Invalid pin!")
        self.menu()
    

    def check_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.pin():
            print(f"Your balance is: ${self.balance}")

        else:
            print("Invalid pin!")
        self.menu()

    def withdraw_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.pin():
            withdrawl_amount = int(input("Enter the the withdrawl amount: "))
            if withdrawl_amount <= self.balance:
                self.balance = self.balance - withdrawl_amount
                print(f"You have withdrawn ${withdrawl_amount}. Your new balance is now: ${self.balance}")
                self.menu()
            else:
                print(f"${withdrawl_amount} exceeds your balance!")
                self.menu()
        else:
            print("Invalid pin!")
        self.menu()


obj = AtmMachine()      