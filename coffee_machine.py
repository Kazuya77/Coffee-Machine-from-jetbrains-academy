water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))

available_cups = min((water // 200), (milk // 50), (beans // 15))

if cups == available_cups:
    print("Yes, I can make that amount of coffee")
elif cups < available_cups:
    print("Yes, I can make that amount of coffee(and even", available_cups - cups, "more than that)")
else:
    print("No, I can make only", available_cups, "cups of coffee")

def statement():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def espresso():
    global water, beans, cups, money
    water -= 250
    beans -= 16
    cups -= 1
    money += 4
    return

def latte():
    global water, milk, beans, cups, money
    water -= 350
    milk -= 75
    beans -= 20
    cups -= 1
    money += 7
    return

def cappuccino():
    global water, milk, beans, cups, money
    water -= 200
    milk -= 100
    beans -= 12
    cups -= 1
    money += 6
    return

action = input("Write action (buy, fill, take):")

if action == "buy":
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    if choice == 1:
        espresso()
    elif choice == 2:
        latte()
    elif choice == 3:
        cappuccino() 
elif action == "fill":
    water += int(input("Write how many ml of water do you want to add:"))
    milk += int(input("Write how many ml of milk do you want to add:"))
    beans += int(input("Write how many grams of coffee beans do you want to add:"))
    cups 
elif action == "take":

statement()
