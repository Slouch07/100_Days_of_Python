from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

powered_on = True
while powered_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        powered_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        beverage = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(beverage):
            if money_machine.make_payment(beverage.cost):
                coffee_maker.make_coffee(beverage)