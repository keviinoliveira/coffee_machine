class money:
    def __init__(self):
        self.teller = 0
        self.received = 0
        self.coins = {
            "penny" : 0.01, 
            "nickel" : 0.05, 
            "dime" : 0.10,
            "quarter" : 0.25
        }
    
    def report(self):
        print(f"Money: ${self.teller}")

    def cash(self):
        print("Please insert coins.")
        quarter= float(input("How many quarters?: "))
        dime = float(input("How many dimes?: "))
        nickel = float(input("How many nickles?: "))
        penny = float(input("How many pennies?: "))
        self.received =  (quarter * self.coins["quarter"]) + (dime * self.coins["dime"]) + (nickel * self.coins["nickel"]) + (penny * self.coins["penny"])
        return self.received

    def check_money(self, menu):
        self.cash()
        if menu > self.received:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        change = self.received - menu
        print(f"Here is ${round(change, 2)} in change")
        self.teller += menu
        return True