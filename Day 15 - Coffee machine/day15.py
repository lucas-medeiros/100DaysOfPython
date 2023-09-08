# @author   Lucas Cardoso de Medeiros
# @since    15/06/2022
# @version  1.0

# Coffee machine


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

profit = 0.0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_ingredients(option):
    """Returns the ingredients necessary to make the selected coffee"""
    return MENU[option]["ingredients"]


def get_cost(option):
    """Returns the price of the selected coffee"""
    return MENU[option]["cost"]


def increment_profit(value):
    """Increments value to the global variable profit"""
    global profit
    profit += value


def use_resource(resource, value):
    """Decrements the resources used to make the coffee"""
    global resources
    resources[resource] -= value


def print_report():
    """Prompts the Coffee Machine report"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(option):
    """Checks if there is enough resources to make the coffee. Returns False if there is not enough"""
    ingredients = get_ingredients(option)
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def get_coins(option):
    """Gets the money input.
    Returns False if there is not enough money.
    Prints the change, if there is change and increase the profit"""
    print("Please insert coins")
    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickles = int(input("How many nickles? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

    cost = get_cost(option)
    if cost > total:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total - cost, 2)
        if change > 0:
            print(f"\nHere is ${change} dollars in change")
        increment_profit(cost)
        return True


def make_coffee(option):
    """Makes the coffee requested."""
    ingredients = get_ingredients(option)
    for item in ingredients:
        use_resource(item, ingredients[item])
    print(f"Here is your {option}. Enjoy!")
    return True


def run_machine():
    """Main coffee machine logic"""
    run = True
    while run:
        option = input("\nWhat would you like? \n"
                       " - Espresso\n"
                       " - Latte\n"
                       " - Cappuccino\n"
                       " - Report\n"
                       " - Off\n").lower()
        if option == "off":
            run = False
            return
        elif option == "report":
            print_report()
        elif option == "espresso" or option == "latte" or option == "cappuccino":
            if check_resources(option):
                if get_coins(option):
                    make_coffee(option)
        else:
            print("Error. Invalid input")
    return


if __name__ == '__main__':
    while input("Do you want to turn 'on' the Coffee Machine? Type 'y' or 'n': ") == 'y':
        run_machine()
