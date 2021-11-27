class Atm:
    def __init__(self,cardno,pinno,balance):
        self.cardno = cardno
        self.pinno = pinno
        self.balance = balance
    def checkBalance(self):
        print("Balance is ",self.balance)
    def withdrew(self,amount):
        newamount = (self.balance)-amount
        print("You withdrew ",newamount)
def main():
    Card_number = input("Enter your card number")
    Pin_number = input("Enter you pin number")
    balance = int(input("Enter the balance amount"))
    amount = int(input("Enter the amount that you have to withdraw"))
    t1 = Atm(Card_number,Pin_number,balance)
    t1.checkBalance()
    t1.withdrew(amount)
main()
