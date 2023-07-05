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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient(ingri):
    for item in ingri:
        if ingri[item]> resources[item]:
            print(f"Sorry, There is not sufficient {item} .")
            return False
    return True
def process_coin():
    total=int(input("Enter the number of Quayers: "))*0.25 + int(input("Enter the number of Dimes: "))*0.10 + int(input("Enter the number of Nickles: "))*0.5 + int(input("Enter the no of Pennies: "))*0.1
    return total
def check_transaction(payment,cost):
    if (payment<cost):
        print("Sorry there no enough money you entered to process request")
        return False
    if payment>=cost:
        refund=round(payment-cost,2)
        global profit
        profit+=cost
        print(f"Your Request is processing, Here is your {refund} .")
        return True

def make_coffee(drink,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f" Here is your {drink}.☕ ")


start=True
while start:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="report":
        print(f' water: {resources["water"]} \n milk: {resources["milk"]} \n Coffee: {resources["coffee"]} \n Money: {profit} ')
    elif choice=="off":
        print("Coffee Machine is switched Off")
        start=False
    else:
        product=MENU[choice]
        if resource_sufficient(product["ingredients"]):
            money=process_coin()
            if check_transaction(payment=money,cost=product["cost"]):
                make_coffee(choice,product["ingredients"])




