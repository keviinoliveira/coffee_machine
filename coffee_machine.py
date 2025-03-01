from coffee_maker import coffe
from money_machine import money
from menu import COFFEES


coffe_maker = coffe()
money_machine = money()
menu = COFFEES

condiction = True
while condiction:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        coffe_maker.report()
        money_machine.report()
    elif coffee_type == "off":
        condiction = False
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        if coffe_maker.check_resources(menu[coffee_type]) and money_machine.check_money(menu[coffee_type]["price"]):
            coffe_maker.update_resources(menu[coffee_type])
            coffe_maker.choose_coffee(coffee_type)
    else:
        print("Please, try again!")