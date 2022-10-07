from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    order_name = input(f"What would you like? ({menu.get_items()})\n -> ")
    if order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "off":
        is_on = False
    else:
        coffee = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)