# @author   Lucas Cardoso de Medeiros
# @since    18/06/2022
# @version  1.0

# Coffee machine - OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def run_machine():
    """Main coffee machine logic"""
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    while True:
        option = input(f"\nWhat would you like? {menu.get_items()}: ").lower()
        if option == "off":
            return
        elif option == "report":
            coffee_maker.report()
            money_machine.report()
        elif option in menu.get_items().split('/'):
            drink = menu.find_drink(option)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            print("Error. Invalid input")
    return


if __name__ == '__main__':
    while input("Do you want to turn 'on' the Coffee Machine? Type 'y' or 'n': ") == 'y':
        run_machine()
