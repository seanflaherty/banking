
class AtmMachine:
    # static variable
    __customer_id = 0

    def __init__ (self):
        self.__pin = ""
        self.__balance = 0
        self.customer_id = AtmMachine.customer_id
        AtmMachine.customer_id += 1
        self.__menu()

    # customer_id getter
    @staticmethod
    def get_customer_id():
        return AtmMachine.__customer_id
    
    # pin getter
    def get_pin(self):
        return self.__pin

    # pin setter
    def set_pin(self, new_pin):
        self.__pin == new_pin

    # balance getter
    def get_balance(self):
        return self.__balance
    
    # balance setter
    def set_balance(self, new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Please enter a number.")
    


    def __menu(self):
        user_input = input(
            """
            Hi how can i help you?

            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balence
            4. Press 4 to withdraw
            5. Any other character to exit
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
        self.__pin = user_pin

        user_balance = int(input("Enter Balance: "))
        self.__balance - user_balance

        print("Pin created successfully")
        self.__menu()

    def change_pin(self):
        old_pin = input("Enter your old pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new pin: ")
            self.__pin = new_pin
            print("Pin changed successfully!")
            self.__menu()
        else:
            print("Invalid pin!")
        self.__menu()
    

    def check_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.__pin():
            print(f"Your balance is: ${self.__balance}")

        else:
            print("Invalid pin!")
        self.__menu()

    def withdraw_balance(self):
        user_pin = input("Enter your pin: ")

        if user_pin == self.pin():
            withdrawl_amount = int(input("Enter the the withdrawl amount: "))
            if withdrawl_amount <= self.__balance:
                self.__balance = self.__balance - withdrawl_amount
                print(f"You have withdrawn ${withdrawl_amount}. Your new balance is now: ${self.__balance}")
                self.__menu()
            else:
                print(f"${withdrawl_amount} exceeds your balance!")
                self.__menu()
        else:
            print("Invalid pin!")
        self.__menu()

class Customer:
    def __init__(self, name, gender, address, ):
        self.name = name
        self.gender = gender
        self.address = address

    def print_info(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Address: {self.address.city}, {self.address.state}, {self.address.zip_code}")

class Address:
    def __init__ (self, city, state, zip_code):
        self.city = city
        self.state = state
        self.zip_code = zip_code

adds = Address("Baltimore", "Maryland", "20112")
cust = Customer("Dave", "Male", adds) 

cust.print_info()