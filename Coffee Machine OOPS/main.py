from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("Welcome to the Coffee Maker!")

coffee_menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

turn_off = False

while not turn_off:
    choice = input("What would you like to have today?(" + coffee_menu.get_items() + ") ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        turn_off = True
    else:
        drink = coffee_menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)




