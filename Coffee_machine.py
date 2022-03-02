from Coffee_report import MENU 
from Coffee_report import resources
from prettytable import PrettyTable

want = True
print("""""""""
   _____   _____           _____            ______  ______ 
  / ____| / ____|         / ____|    /\    |  ____||  ____|
 | |     | (___  ______  | |        /  \   | |__   | |__   
 | |      \___ \|______| | |       / /\ \  |  __|  |  __|  
 | |____  ____) |        | |____  / ____ \ | |     | |____ 
  \_____||_____/          \_____|/_/    \_\|_|     |______|
                                                           
                                                           
""""""""")

def menu():
    print("Welcome to CS CAFE: ")
    print("****☕Coffee Available☕ ****")
    menucard = PrettyTable(['Coffee☕','Cost₹'])
    menucard.add_row(['Espresso',MENU['espresso']['cost']])
    menucard.add_row(['Latte',MENU['latte']['cost']])
    menucard.add_row(['Cappuccino',MENU['cappuccino']['cost']])
    print(menucard)

def check_water(x):
    saman = MENU[x]['ingredients']
    if resources['water']>=saman['water']:
        resources['water'] = resources['water'] - saman['water']
        return 1
    else:
        return 0
def check_milk(x):
    saman = MENU[x]['ingredients']
    if resources['milk']>=saman['milk']:
        resources['milk'] = resources['milk'] - saman['milk']
        return 1
    else:
        return 0

def check_coffee(x):
    saman = MENU[x]['ingredients']
    if resources['coffee']>saman['coffee']:
        resources['coffee'] = resources['coffee'] - saman['coffee']
        return 1
    else:
        return 0

def paise_de(x):
    paisa = MENU[x]['cost']
    print("Please insert coins !!:")
    count = 0
    ten_rupee = int(input("Count of 10₹ coins"))
    count+= ten_rupee*10

    five_rupee = int(input("Count of 5₹ coins"))
    count+= five_rupee*5

    two_rupee = int(input("Count of 2₹ coins"))
    count+= two_rupee*2

    one_rupee = int(input("Count of 1₹ coins"))
    count+= one_rupee*1
    if paisa<count:
        change = count-paisa
        print(f"Here is your Change {change} ₹")
        print(f"Here is your {x} enjoy!!! ☕")
    elif paisa>count:
        print("Sorry this is money is no enough \n your money is refunded")
        saman = MENU[x]['ingredients']
        ing = list(saman.keys())

        for i in ing:
            resources[i] = resources[i] + saman[i]

        count = 0
    else:
        print(f"Here is your {x} enjoy!!! ☕")


def espresso():
    #    "espresso": {
    #    "ingredients": {
    #        "water": 50,
    #        "coffee": 18,
    #    },
    #    "cost": 133,
    #}
    #pass
    water = check_water('espresso')
    coffee = check_coffee('espresso')
    #print(water)
    #print(resources['water'])
    if water == 1 and coffee == 1:
        paise_de('espresso')


    if water == 0:
        saman = MENU['espresso']['ingredients']
        if coffee == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
        print("Sorry not enough water in the tank 😪😪")
    elif coffee == 0:
        saman = MENU['espresso']['ingredients']
        if water == 1:
            resources['water'] = resources['water'] + saman['water']
        print("Sorry not enough coffee in the tank 😪😪")
    else:
        pass

def latte():
    #    "latte": {
    #    "ingredients": {
    #        "water": 200,
    #       "milk": 150,
    #        "coffee": 24,
    #    },
    #    "cost": 188,
    #}
    water = check_water('latte')
    coffee = check_coffee('latte')
    milk = check_milk('latte')
    #print(water)
    #print(resources['water'])
    if water == 1 and coffee == 1 and milk==1:
        paise_de('latte')


    if water == 0:
        saman = MENU['latte']['ingredients']
        if coffee == 1 and milk == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
            resources['milk'] = resources['milk'] + saman['milk']
        elif coffee ==0 and milk ==1:
            resources['milk'] = resources['milk'] + saman['milk']
        elif coffee == 1 and milk == 0:
            resources['coffee'] = resources['coffee'] + saman['coffee']
        print("Sorry not enough water in the tank 😪😪")
    elif coffee == 0:
        saman = MENU['latte']['ingredients']
        if water == 1 and milk == 1:
            resources['water'] = resources['water'] + saman['water']
            resources['milk'] = resources['milk'] + saman['milk']
        elif water == 0 and milk == 1:
            resources['milk'] = resources['milk'] + saman['milk']
        elif water == 1 and milk == 0:
            resources['water'] = resources['water'] + saman['water']
        print("Sorry not enough coffee in the tank 😪😪")
    elif milk == 0:
        saman = MENU['latte']['ingredients']
        if water == 1 and coffee == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
            resources['water'] = resources['water'] + saman['water']
        elif water == 1 and coffee == 0:
            resources['water'] = resources['water'] + saman['water']
        elif water == 0 and coffee == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
        print("Sorry not enough milk in the tank 😪😪")





def cappuccino():
    #"cappuccino": {
    #    "ingredients": {
    #        "water": 250,
    #        "milk": 100,
    #        "coffee": 24,
    #    },
    #    "cost": 225,
    #}
    water = check_water('cappuccino')
    coffee = check_coffee('cappuccino')
    milk = check_milk('cappuccino')
    #print(water)
    #print(resources['water'])
    if water == 1 and coffee == 1 and milk==1:
        paise_de('cappuccino')


    if water == 0:
        saman = MENU['cappuccino']['ingredients']
        if coffee == 1 and milk == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
            resources['milk'] = resources['milk'] + saman['milk']
        elif coffee ==0 and milk ==1:
            resources['milk'] = resources['milk'] + saman['milk']
        elif coffee == 1 and milk == 0:
            resources['coffee'] = resources['coffee'] + saman['coffee']
        print("Sorry not enough water in the tank 😪😪")
    elif coffee == 0:
        saman = MENU['cappuccino']['ingredients']
        if water == 1 and milk == 1:
            resources['water'] = resources['water'] + saman['water']
            resources['milk'] = resources['milk'] + saman['milk']
        elif water == 0 and milk == 1:
            resources['milk'] = resources['milk'] + saman['milk']
        elif water == 1 and milk == 0:
            resources['water'] = resources['water'] + saman['water']
        print("Sorry not enough coffee in the tank 😪😪")
    elif milk == 0:
        saman = MENU['cappuccino']['ingredients']
        if water == 1 and coffee == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
            resources['water'] = resources['water'] + saman['water']
        elif water == 1 and coffee == 0:
            resources['water'] = resources['water'] + saman['water']
        elif water == 0 and coffee == 1:
            resources['coffee'] = resources['coffee'] + saman['coffee']
        print("Sorry not enough milk in the tank 😪😪")


while want:
    menu()
    order = input("What you want to Order? (espresso/latte/cappuccino/bye to exit the machine/report to check the tank): ")
    if order == "report":
        print("Water: ",resources['water'])
        print("Milk: ",resources['milk'])
        print("Coffee: ",resources['coffee'])
    elif order == "espresso":
        print("order",order)
        espresso()
    elif order == "latte":
        print("order",order)
        latte()
    elif order == "cappuccino":
        print("order",order)
        cappuccino()
    elif order == 'bye':
        exit()
    else:
        print("Unknown order!!!")

