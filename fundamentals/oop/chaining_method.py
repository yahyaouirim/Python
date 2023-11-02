class User:		
    def __init__(self):
        self.name = "Rim"
        self.amount = 0
    def make_depposit(self, amount):
        self.amount+=amount
        return self

    def make_withdrawal(self, amount):
        self.amount-=amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} Balance: {self.amount}")
        return self

    def transfer_money(self, other_user, amount):
        self.amount-=amount
        other_user.amount+=amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

Sarra=User()
Sarra.name="Sarra"
Kouba=User()
Kouba.name="Kouba"
Alaa=User()
Alaa.name="Alla"
Sarra.make_depposit(500).make_depposit(1000).make_depposit(200).make_withdrawal(100).display_user_balance()
Kouba.make_depposit(300).make_depposit(700).make_withdrawal(250).make_withdrawal(150).display_user_balance()
Alaa.make_depposit(1200).make_withdrawal(300).make_withdrawal(100).make_withdrawal(200).display_user_balance()
Sarra.transfer_money(Alaa, 3000)
