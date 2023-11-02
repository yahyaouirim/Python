# declare a class and give it name User
class User:		
    def __init__(self):
        self.name = "Rim"
        self.amount = 0
    def make_depposit(self, amount):
        self.amount+=amount

    def make_withdrawal(self, amount):
        self.amount-=amount

    def display_user_balance(self):
        print(f"User: {self.name} Balanve: {self.amount}")

    def transfer_money(self, other_user, amount):
        self.amount-=amount
        other_user.amount+=amount
        self.display_user_balance()
        other_user.display_user_balance()



Sarra=User()
Sarra.name="Sarra"
Kouba=User()
Kouba.name="Kouba"
Alaa=User()
Alaa.name="Alla"
Sarra.make_depposit(500)
Sarra.make_depposit(1000)
Sarra.make_depposit(200)
Sarra.make_withdrawal(100)
Sarra.display_user_balance()
Kouba.make_depposit(300)
Kouba.make_depposit(700)
Kouba.make_withdrawal(250)
Kouba.make_withdrawal(150)
Kouba.display_user_balance()
Alaa.make_depposit(1200)
Alaa.make_withdrawal(300)
Alaa.make_withdrawal(100)
Alaa.make_withdrawal(200)
Alaa.display_user_balance()
Sarra.transfer_money(Alaa, 3000)








