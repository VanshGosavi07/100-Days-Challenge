from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = MoneyMachine()
coffee_maker = CoffeeMaker()
my_menu = Menu()


while (1):
    drink = input(f"Enter what you want {my_menu.get_items()} : \n")
    if drink == 'off':
        exit(1)
    elif drink == 'report':
        coffee_maker.report()
        machine.report()
    else:
        drink = my_menu.find_drink(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

