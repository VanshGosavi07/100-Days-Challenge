from pickle import GLOBAL

from MENU import MENU

resource = {
    "Water": 300,
    "Milk": 200,
    "Cofee": 100,
    "profit": 0,
}


def purchase(choice):
    resource["Water"] -= MENU[choice]["ingredients"]['water']
    resource["Milk"] -= MENU[choice]["ingredients"]['milk']
    resource["Cofee"] -= MENU[choice]["ingredients"]['coffee']
    print(f"Here is your {choice} ☕️. Enjoy!")


def insert_coin(choice):
    print("Please Insert coins")
    quarters = 0.25 * float(input("Enter Quarters :"))
    dimes = 0.10 * float(input("Enter dimes :"))
    nickel = 0.05 * float(input("Enter nickel :"))
    pennies = 0.01 * float(input("Enter pennies :"))
    money = (quarters + dimes + nickel + pennies)
    if (money >= MENU[choice]['cost']):
        resource['profit'] += MENU[choice]['cost']
        print(f"Here is ${round(money-MENU[choice]['cost'],3)} in change")
        purchase(choice)
    else:
        print("Insert More Money")


def resource_check(choice):
    if (resource["Water"] >= MENU[choice]["ingredients"]['water']) and (
            resource["Milk"] >= MENU[choice]["ingredients"]['milk']) and (
            resource["Cofee"] >= MENU[choice]["ingredients"]['coffee']):
        insert_coin(choice)
    else:
        print('Resources Not Available')
        exit(1)


while (1):
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"Water: {resource['Water']}ml")
        print(f"Milk: {resource['Milk']}ml")
        print(f"Cofee: {resource['Cofee']}g")
        print(f"Money: ${resource['profit']}")
    elif choice == 'espresso':
        resource_check(choice)
    elif choice == 'latte':
        resource_check(choice)
    elif choice == 'cappuccino':
        resource_check(choice)
    else:
        print("Invalid Input")
        exit(1)
