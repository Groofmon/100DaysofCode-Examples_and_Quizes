from CoffeeMenu import MENU, resources


def coffee_choice():
    """ Defining which coffee user wants to drink. """
    while True:
        choice = input("What would you like? (espresso, latte, cappuccino): ")
        if choice in [i for i in MENU.keys()]:
            break
        elif choice == "report":
            print(f"""water: {resources["water"]}
"milk": {resources["milk"]}
"coffee": {resources["coffee"]}
""")
            continue
        elif choice == "off":
            exit()
        else:
            continue

    recipe_water = MENU[choice]["ingredients"]["water"]
    recipe_coffee = MENU[choice]["ingredients"]["coffee"]
    if choice != "espresso":
        recipe_milk = MENU[choice]["ingredients"]["milk"]

    # espresso
    if choice == "espresso" and resources["water"] >= recipe_water and resources["coffee"] >= recipe_coffee:
        # resources["water"] -= recipe_water
        # resources["coffee"] -= recipe_coffee
        return choice

    # latte and cappuccino
    elif (choice != "espresso" and resources["water"] >= recipe_water and resources["coffee"] >= recipe_coffee
          and resources["milk"] >= recipe_milk):
        # resources["water"] -= recipe_water
        # resources["coffee"] -= recipe_coffee
        # resources["milk"] -= recipe_milk
        return choice

    else:
        if resources["water"] < recipe_water:
            print(f"Sorry, There is not enough water to make {choice}")
            return False
        elif resources["coffee"] < recipe_coffee:
            print(f"Sorry, There is not enough coffee to make {choice}")
            return False
        elif choice != "espresso" and resources["milk"] < recipe_milk:
            print(f"Sorry, There is not enough milk to make {choice}")
            return False


def process_coins(coffee_type):
    """ Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 """
    print(f"Please, insert ${format(MENU[coffee_type]["cost"], '.2f')} coins!")
    quarters = int(input("quarters($0.25): "))
    dimes = int(input("dimes($0.10): "))
    nickles = int(input("dimes($0.05): "))
    pennies = int(input("pennies($0.01): "))
    global total_coin
    total_coin = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    if MENU[coffee_type]["cost"] <= total_coin:
        return True
    else:
        print(f"Sorry, {coffee_type} is ${MENU[coffee_type]["cost"]}, but you only have ${format(total_coin, '.2f')}")
        return False


# ---------------------main.p-----------------------------
while True:
    print(f"""- water: {resources["water"]} 
- milk: {resources["milk"]} 
- coffee: {resources["coffee"]}""")
    coffee_type = coffee_choice()
    if coffee_type != False:
        IsPayed = process_coins(coffee_type)
    else:
        continue

    if IsPayed == True:

        if coffee_type == "espresso":
            resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
            print(f"Here is your hot espresso☕. refund: ${format(total_coin - MENU[coffee_type]["cost"], '.2f')}")

        elif coffee_type != "espresso":
            resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
            resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
            resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
            print(f"Here is your hot {coffee_type}☕. refund: ${format(total_coin - MENU[coffee_type]["cost"], '.2f')}")





