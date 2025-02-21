COFFEES = {
    "espresso" : {"water" : 50, "coffee" : 18, "price" : 1.5},
    "latte" : {"water": 200, "coffee" : 24, "milk" : 150, "price" : 2.5},
    "cappuccino" : {"water" : 250, "coffee" : 24, "milk" : 100, "price" : 3.0} }
COINS = {"penny" : 0.01, "nickel" : 0.05, "dime" : 0.10, "quarter" : 0.25}

def resources(machine):
    for resources in machine:
        if resources == "water" or resources == "milk":
            print(f"{resources}: {machine[resources]}ml")
        elif resources == "coffee":
            print(f"{resources}: {machine[resources]}g")
        elif resources == "money":
            print(f"{resources}: ${machine[resources]}")

def check_resources(coffee_type, resources):
    resources_bad = ""
    count = 0
    for item in COFFEES[coffee_type]:
        if item != "price":
            if resources[item] - COFFEES[coffee_type][item] < 0:
                if count ==0 :
                    resources_bad += item
                else: 
                    resources_bad += ", " + item
                count =+ 1
    if count > 0:
        print(f"Sorry there is not enough {resources_bad}")
        return False
    return True  

def update_resources(coffee_type, resources):
    for item in COFFEES[coffee_type]:
        if item != "price":
            resources[item] -= COFFEES[coffee_type][item]
        else:
            resources["money"] += COFFEES[coffee_type]["price"]
    return resources  

def cash():
    print("Please insert coins.")
    quarter= float(input("How many quarters?: "))
    dime = float(input("How many dimes?: "))
    nickel = float(input("How many nickles?: "))
    penny = float(input("How many pennies?: "))
    return (quarter * COINS["quarter"]) + (dime * COINS["dime"]) + (nickel * COINS["nickel"]) + (penny * COINS["penny"])

def choose_coffee(coffee_type, resources):
    if check_resources(coffee_type, resources) == False:
        return 
    cash_client = cash()
    if COFFEES[coffee_type]["price"] > cash_client:
        print("Sorry, that's not enough money. Money refunded.")
        return
    change = cash_client - COFFEES[coffee_type]["price"] 
    print(f"Here is ${round(change, 2)} in change")
    print(f"Here is your {coffee_type} ☕ Enjoy!")
    update_resources(coffee_type, resources)
    return resources

resources_machine = {"water" : 300, "coffee" : 100, "milk" : 200, "money" : 0}
condiction = True
while condiction:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        resources(resources_machine)
    elif coffee_type == "off":
        condiction = False
    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        choose_coffee(coffee_type, resources_machine)
    else:
        print("Please, try again!")
