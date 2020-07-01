from time import sleep


class DemirBank:
    __balance = 0 #protected data
    __id = 0 #private data
    _personal_info = {} #protected data

#magic function
    def  __init__(self, name, surname, amount, id):
        self._personal_info['name'] = name
        self._personal_info['surname'] = surname
        if amount > 0:
            self.__balance = amount
        elif amount == 0:
            raise ValueError('Amount must be zero')
        self.__id = id
            
     def deposit(self, amount):
        if amount>0:
            print("Operation process...")
            sleep(2)
            self.__balance += amount
            print("your balance is ", self.__balance)
        else:
            print('Invalid amount')

    def withdraw(self, amount):
        if amount>0 and amount<self.__balance:
            print('Money transfering...')
            sleep(2)
            self.__balance -= amount
            print("Your balance now is ", self.__balance)
        else:
            print('Invalid amount')
    
    def check_balance(self):
        #do something
        print("Your balance is {self.__balance}")
