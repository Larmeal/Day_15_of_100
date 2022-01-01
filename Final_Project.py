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









