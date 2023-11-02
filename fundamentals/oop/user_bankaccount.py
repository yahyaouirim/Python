class BankAccount:
    all_accounts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        self.balance=balance
        self.int_rate=int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if(self.balance-amount)<0:
            print( "Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self
    def display_account_info(self):
        print(f"Balance : {self.balance}")
        return self
    def yield_interest(self):
        if self.balance >0:
            self.balance+=(self.balance*self.int_rate)
        return self
    #class method
    @classmethod
    def bankaccount_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()

# declare a class and give it name User
class User:		
    def __init__(self, name):
        self.name = name
        self.amount = 0
        self.account = BankAccount(int_rate=0.02, balance=0)# added this line


    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.account.balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.amount-=amount
        other_user.amount+=amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

youssef=User("Youssef")
youssef.account.deposit(100).deposit(300)
youssef.display_user_balance()