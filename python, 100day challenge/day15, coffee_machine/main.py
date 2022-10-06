import data


def admin_mode(menu):
    global money
    if menu == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}g")
        print(f"Money: ${money}")
        coffe_machine()

    if menu == "off":
        exit()


def payment(menu):
    global money
    cost = data.MENU[menu]['cost']
    print("Please insert coins.")
    bill = 0

    for coin in data.coins:
        pay = float(input(f"how many {coin}?: "))
        bill += pay * data.coins[coin]

    if bill < cost:
        print("Sorry that's not enough money. Money refunded")
        bill = 0
        coffe_machine()
    elif bill == cost:
        print("It's perfect. I don't have any change for you")
        money += cost
    else:
        print(f"Here is ${round(bill - cost, 3)} in change.")
        money += cost


money = 0


def coffe_machine():
    global money

    menu = input("What would you like? (espresso/latte/cappuccino)\n -> ")
    admin_mode(menu)

    recipe = data.MENU[menu]["ingredients"]

    for material in data.resources:
        if data.resources[material] < recipe[material]:
            print(f"Sorry there is not enough {material}.")
            coffe_machine()

    payment(menu)

    for i in data.resources:
        data.resources[i] -= recipe[i]

    print(f"Here is your {menu} ☕️. Enjoy!")
    coffe_machine()


coffe_machine()
