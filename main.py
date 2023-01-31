QUARTERS = 0.25
DIMES = 0.10
PENNIES = 0.01
NICKLES = 0.05

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

should_continue = True
while should_continue:
    coffee_select = input("What would you like (espresso/latte/cappuccino): ").lower()

    def update_resources(types):
        """Deduct the required ingredients from the resources."""
        resources["water"] = resources["water"] - MENU[types]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[types]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[types]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU[types]["cost"]
                

    def process_coin(types):
        """Checks if the money is sufficient to make coffee."""
        quarters = float(input("How many quarters?: "))
        dimes = float(input("How many dimes?: "))
        nickles = float(input("How many nickles?: "))
        pennies = float(input("How many quarters?: "))
        total_cost = (quarters*QUARTERS) + (dimes*DIMES) + (nickles*NICKLES) + (pennies*PENNIES)
        if total_cost >= MENU[types]["cost"]:
            total_return = round((total_cost - MENU[types]["cost"]), 2)
            print(f"Here is ${total_return} in change.")
            print(f"Here is your {types}☕️ Enjoy!")
            update_resources(types)
        elif total_cost < MENU[types]["cost"]:
            print("Sorry that's not enough money. Money refunded.")

    def check_availability(ingredients):
        """Checks if the ingredients are sufficient to make coffee."""
        for items in ingredients:
            if ingredients[items] > resources[items]:
                print(f"Sorry! there is not enough {items}")
                return False
        return True
    

    if coffee_select == "off":
        print("Under Maintainance. Sorry for the inconvenience")
        should_continue = False
    elif coffee_select == "report":
        print(f'Water: {resources["water"]}ml\n Milk: {resources["milk"]}ml\n Coffee: {resources["coffee"]}g\n Money: ${resources["money"]}')
    elif coffee_select == "espresso" or "latte" or "cappuccino":
        order_ingredients = MENU[coffee_select]["ingredients"]
        if check_availability(order_ingredients):
            process_coin(coffee_select)


       
