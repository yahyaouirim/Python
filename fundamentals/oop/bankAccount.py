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

Hb=BankAccount(0.05, 1000)
Stb=BankAccount(0.03, 1200)

Hb.deposit(200).deposit(300).deposit(500).withdraw(400).yield_interest().display_account_info()
Stb.deposit(3000).deposit(900).withdraw(200).withdraw(230).withdraw(500).withdraw(800).yield_interest().display_account_info()
BankAccount.bankaccount_info()


