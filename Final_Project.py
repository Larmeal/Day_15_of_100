#สร้างเครื่องทำกาแฟ

from main import MENU, resources, coin
from art import logo, coffee

#ระบบหลังบ้าน(การสร้างกาแฟ)
remain_supply = [resources["water"], resources["milk"], resources["coffee"]]
print(logo)

def order():
    expenditure = input("Please insert coins. Type quarters, dimes, nickels, pennies: $").split(", ")
    expand = float(expenditure[0])*coin["quarters"] + float(expenditure[1])*coin["dimes"] + float(expenditure[2])*coin["nickels"] + float(expenditure[3])*coin["pennies"]
    if expand > MENU[order_MENU]["cost"]:
        remain = expand - MENU[order_MENU]["cost"]
        print(f"Thank you for your order this is your chance: {remain}$")
        if remain_supply[0] < MENU[order_MENU]["ingredients"]["water"]:
            print("Sorry there is not enough water ")
        if remain_supply[1] < MENU[order_MENU]["ingredients"]["milk"]:
            print("Sorry there is not enough milk ")
        if remain_supply[2] < MENU[order_MENU]["ingredients"]["coffee"]:
           print("Sorry there is not enough MENU")
        else:
            print(f"""Here is your {order_MENU}
            {coffee} 
Enjoy!""")
           
    elif expand < MENU[order_MENU]["cost"]:
        remain = MENU[order_MENU]["cost"] - expand
        print(f"Sorry you lack money about: {remain}$")
        expenditure = input("Please insert coins more. Type quarters, dimes, nickels, pennies: $").split(", ")
    


#คำนวณวัตถุดิบ และการเติม วัตถุดิบ
def supply():
    for i in MENU[order_MENU]["ingredients"]:
        resources[i] -= MENU[order_MENU]["ingredients"][i]


def ask_again():
    order_again = input("Do you need anything else? 'yes' or 'no': ").lower()
    if order_again == "no":
        again = False
        print("Have a nice day, See you later")
    else:
        again = True
#เมนู
again = True
while again:
    order_MENU = input("What would you like? (Espresso/Latte/Cappuccino): ").lower()
    if order_MENU == "report" and order_MENU != "add" or order_MENU != "report" and order_MENU == "add":
        if order_MENU == "report":
            print(f"""
Water: {resources["water"]} ml
Milk: {resources["milk"]} ml
Coffee: {resources["coffee"]} g
""")
        
        elif order_MENU == "add":
            add_supply = input("How much are you want to add the supply water/milk/coffee: ").split(",")
            add_supply_dict = {
                "water": int(add_supply[0]),
                "milk": int(add_supply[1]),
                "coffee": int(add_supply[2]),
                }
            for i in add_supply_dict:
                resources[i] += add_supply_dict[i]
            ask_again()
            
    elif order_MENU == "no":
        again = False
        print("Have a nice day, See you later")
        
    else:
        price_MENU = MENU[order_MENU]["cost"]
        print(f"the prices is {price_MENU}$")
        
    #ระบบหน้าบ้าน
        if order_MENU == "espresso":
            order()
        elif order_MENU == "latte":
            order()
        elif order_MENU == "cappuccino":
            order()
        supply()
        ask_again()
       
# My teacher version

# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }

# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }


# def is_resource_sufficient(order_ingredients):
#     """Returns True when order can be made, False if ingredients are insufficient."""
#     for item in order_ingredients:
#         if order_ingredients[item] > resources[item]:
#             print(f"​Sorry there is not enough {item}.")
#             return False
#     return True


# def process_coins():
#     """Returns the total calculated from coins inserted."""
#     print("Please insert coins.")
#     total = int(input("how many quarters?: ")) * 0.25
#     total += int(input("how many dimes?: ")) * 0.1
#     total += int(input("how many nickles?: ")) * 0.05
#     total += int(input("how many pennies?: ")) * 0.01
#     return total


# def is_transaction_successful(money_received, drink_cost):
#     """Return True when the payment is accepted, or False if money is insufficient."""
#     if money_received >= drink_cost:
#         change = round(money_received - drink_cost, 2)
#         print(f"Here is ${change} in change.")
#         global profit
#         profit += drink_cost
#         return True
#     else:
#         print("Sorry that's not enough money. Money refunded.")
#         return False


# def make_coffee(drink_name, order_ingredients):
#     """Deduct the required ingredients from the resources."""
#     for item in order_ingredients:
#         resources[item] -= order_ingredients[item]
#     print(f"Here is your {drink_name} ☕️. Enjoy!")


# is_on = True

# while is_on:
#     choice = input("​What would you like? (espresso/latte/cappuccino): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_transaction_successful(payment, drink["cost"]):
#                 make_coffee(choice, drink["ingredients"])

















