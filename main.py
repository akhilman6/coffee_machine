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

profit = 0

resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
}


def check_resources(order_ingredients):
    """Returns True if order can be made, False if ingredients are not sufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, there is not enough {item}.')
            return False
        return True


def process_coins():
    """Returns the total calculated amount inserted."""
    print("Please enter coins.")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.1
    total += int(input("Nickels: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is successful, False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here's your change: ${change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, order_ingredients):
    """Deduct used ingredients from resources."""
    for item in  order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/capuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])
