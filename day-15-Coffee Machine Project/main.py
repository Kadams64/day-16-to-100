
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
    "money": 0.0,
}


def prompt_user():
    """prompt the user for coffee type"""""
    return input("What would you like? espresso/latte/cappuccino ").lower()


def output_report():
    """output a report reflecting the state of the machines
    stored resources"""
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["coffee"]}g")
    print(f"Money: ${resources["money"]}")


def get_requirements(selection):
    return MENU[selection]["ingredients"]


def get_price(selection):
    return MENU[selection]["cost"]


def have_sufficient_resources(res ):
    """iterate over the 'resources' dictionary item and compare it
    to the machine resources.  Identify any shortfalls in capacity."""
    sufficient = True
    for item in res:
        if res[item] > resources[item]:
            print(f"There is insufficient {item}")
            sufficient = False
    return sufficient


def process_coins():
    """input the coin count and return a total value in pennies"""
    total_value = 0
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))

    total_value += num_quarters * 25
    total_value += num_dimes * 10
    total_value += num_nickels * 5
    total_value += num_pennies
    return total_value / 100


def process_transaction(money, cost, menu_item):
    success = True
    if money < cost:
        success = False
        print(f"Sorry, {money} is not enough for your selected drink. Money refunded.")
    else:
        resources["money"] += cost
        if money > cost:
            # refund any excess
            difference = round(money - cost, 2)
            print(f"You over-paid.  Here is {difference:.2f} in change")
    return success


def subtract_resources(menu_item):
    for res in menu_item:
        resources[res] -= menu_item[res]


def make_coffee(menu_item):
    """make coffee by subtracting resources"""
    print("making coffee")
    subtract_resources(menu_item)


def run_coffee_maker():
    """The main coffee machine operational loop"""
    on = True
    while on:
        choice = prompt_user()
        if choice == "report":
            output_report()
        elif choice == "off":
            print("Exiting coffee operations due to admin command.")
            return  #exit the operational loop
        else:
            if choice in MENU:
                requirements = get_requirements(choice)
                price = get_price(choice)

                # warning regarding python expected type {__iter__, __getitem__} got dict[str, int] |float | int
                # I tried chasing this around for a bit, basically as I understand it PyCharm is being
                # cautious here about type mismatches and I can't really find a good fit solution
                if have_sufficient_resources(requirements):
                    money_deposited = process_coins()
                    if process_transaction(money_deposited, price, choice):
                        make_coffee(requirements)
                        print(f"Here is your {choice}, enjoy!")
                else:
                    print("Sorry: the machine does not have sufficient resources to make your drink")
            else:
                print(f"Your selection, {choice}, is invalid")


run_coffee_maker()
