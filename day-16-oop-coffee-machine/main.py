from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
bank = 0

on = True
while on:
    items = menu.get_items()
    choice = input(f"What would you like? {items} ")
    if choice == "off":
        print("exiting the coffee maker loop")
        on = False
    elif choice == "report":
        maker.report()
        money.report()
    else:
        # find drink returns None for invalid choices, also prints a message
        item = menu.find_drink(choice)
        # make sure that choice is a valid item
        if item is not None:
            if maker.is_resource_sufficient(item):
                # make_payment handles processing coins and both excess and insufficient funds
                if money.make_payment(item.cost):
                    maker.make_coffee(item)

