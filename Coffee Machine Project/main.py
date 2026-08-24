MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
}

QUARTER_VALUE_IN_DOLLARS = 0.25
DIME_VALUE_IN_DOLLARS = 0.10
NICKLE_VALUE_IN_DOLLARS = 0.05
PENNY_VALUE_IN_DOLLARS = 0.01


def generate_report(resources, total_money):
    print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${total_money}")

def check_resource_sufficient(choice):
    actual_water = resources["water"]
    actual_milk = resources["milk"]
    actual_coffee = resources["coffee"]
    if actual_water < MENU[choice]["ingredients"]["water"]:
        print("Sorry, there's not enough water.")
        return False
    elif choice != "espresso" and actual_milk < MENU[choice]["ingredients"]["milk"]:
        print("Sorry, there's not enough milk.")
        return False
    elif actual_coffee < MENU[choice]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee.")
        return False
    return True

def update_resources(choice):
    global resources
    resources["water"] -= MENU[choice]["ingredients"]["water"]
    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        resources["milk"] -= MENU[choice]["ingredients"]["milk"]

def make_coffee(choice):
    global profit
    if check_resource_sufficient(choice) is True:
        cost_of_drink = MENU[choice]["cost"]
        print("Please insert coins.")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))

        total_value_of_coins = (quarters * QUARTER_VALUE_IN_DOLLARS
                                + dimes * DIME_VALUE_IN_DOLLARS
                                + nickels * NICKLE_VALUE_IN_DOLLARS
                                + pennies * PENNY_VALUE_IN_DOLLARS)

        if total_value_of_coins < cost_of_drink:
            print("Sorry, that's not enough money to make a coffee! Money refunded.")
        elif total_value_of_coins >= cost_of_drink:
            change = total_value_of_coins - cost_of_drink
            print(f"Here is ${round(change, 2)} in change.")
            profit += cost_of_drink
            update_resources(choice)
            print(f"Here is your {choice}. Enjoy ur drink.")


turned_off = False
profit = 0

print("Welcome to The Lolli's & Loaf Cafe!")

while not turned_off:
    print(f"Menu:\nEspresso: ${MENU["espresso"]["cost"]}\nLatte: ${MENU["latte"]["cost"]}\nCappuccino: ${MENU["cappuccino"]["cost"]}")
    choice = input("What would you like to have today? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        generate_report(resources, profit)
    elif choice == "off":
        turned_off = True
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        make_coffee(choice)
    else:
        print("Sorry, that's not correct. Please provide valid input.")




