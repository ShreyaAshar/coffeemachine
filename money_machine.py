class MoneyMachine:

    currency = "$"

    coin_val = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_rec = 0

    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        print("Please insert coins.")
        for coin in self.coin_val:
            self.money_rec += int(input(f"How many {coin}?: ")) * self.voin_val[coin]
        return self.money_rec

    def make_payment(self, cost):
        self.process_coins()
        if self.money_rec >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.currency}{change} in change.")
            self.profit += cost
            self.money_rec = 0
            return True
        else:
            print("Sorry, that is not enough money. Money refunded.")
            self.money_rec = 0
            return False
        
