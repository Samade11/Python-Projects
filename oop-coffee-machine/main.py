from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
sufficient_resources = CoffeeMaker().is_resource_sufficient
menu = Menu()


is_on = True
while is_on:
    option = menu.get_items()
    choice = input(f"What would you like? ({option}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if sufficient_resources(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

