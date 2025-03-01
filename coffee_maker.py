class coffe:
    def __init__(self):
        self.resources = {
            "water" : 300, 
            "coffee" : 100, 
            "milk" : 200,
        }

    def report(self):
        for resource in self.resources:
            if resource == "water" or resource == "milk":
                print(f"{resource}: {self.resources[resource]}ml")
            elif resource == "coffee":
                print(f"{resource}: {self.resources[resource]}g")

    def check_resources(self, menu):
        resources_bad = ""
        count = 0
        for item in menu:
            if item != "price":
                if self.resources[item] - menu[item] < 0:
                    if count ==0 :
                        resources_bad += item
                    else: 
                        resources_bad += ", " + item
                    count =+ 1
        if count > 0:
            print(f"Sorry there is not enough {resources_bad}")
            return False
        return True 

    def choose_coffee(self, coffee_type):
        print(f"Here is your {coffee_type} ☕ Enjoy!")
    
    def update_resources(self, menu):
        for item in menu:
            if item != "price":
                self.resources[item] -= menu[item]
