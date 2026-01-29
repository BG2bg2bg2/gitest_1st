


#Create inventory list
#Create gold amount for user
inventory = []
gold = 50

#Ask user to choose a character type
character = input("choose character (human, dog, bear, goblin): ")
#Store character type

#Function inventory_menu
    #Ask user:
        #1. Store item
        #2. Change item
        #3. Quit inventory
def inventory_menu():
    global gold

    while True:
        print("1. store item")
        print("2. change item")
        print("3. quit inventory")

        choice = input("choose: ")
    #If user chooses store item
        #Ask: collect or buy?
    if choice == "1":
            method = input("collect or buy? ")

        #If collect
            #Ask for item name
            #Add item to inventory
    if method == "collect":
        item = input("item name: ")
        inventory.append(item)
        print(item, "added")
        #If buy
        #Show items allowed for the user's character type
         #Ask which item to buy
            #Check if user has enough gold
            #If yes
                #Remove gold
                #Add item to inventory
            #Else
                #Show error message
    elif method == "buy":
                print("items you can buy:")
                for item, price in store_items[character].items():
                    print(item, "-", price, "gold")

                buy_item = input("what do you want to buy? ")

                if buy_item in store_items[character]:
                    price = store_items[character][buy_item]

                    if gold >= price:
                        gold -= price
                        inventory.append(buy_item)
                        print("you bought", buy_item)
                    else:
                        print("not enough gold")
                else:
                    print("item not allowed")


    #If user chooses change item
        #Ask:
            #1. Set soul free
            #2. Use or drop item
    elif choice == "2":
        print("1. set soul free")
        print("2. use or drop item")
        change = input("choose: ")
        #If set soul free
            #Show souls in inventory
            #Ask which soul to free
            #Remove soul from inventory
    if change == "1":
        souls = [i for i in inventory if "soul" in i]

        if souls:
            print("souls:", souls)
            soul = input("which soul to free? ")
        if soul in inventory:
            inventory.remove(soul)
            print("soul freed")
        else:
                    print("no souls in inventory")
        #If use or drop item
            #Ask which item
            #Use or remove item from inventory
    elif change == "2":
        print("inventory:", inventory)
        item = input("which item? ")
        action = input("use or drop? ")

    if item in inventory:
        if action == "use":
            print("you used", item)
        elif action == "drop":
            inventory.remove(item)
            print(item, "dropped")
        else:
                    print("item not found")

    #If user chooses quit
        #Exit inventory and return to game
    elif choice == "3":
        print("leaving inventory")
        break

    else:
            print("invalid choice")

    print("gold:", gold)
    print("inventory:", inventory)
#Character rules:
    #If character is human
        #Can buy: sword, potions, charms, keys

    #If character is dog or bear
        #Can use abilities: bite, run faster
        #Can buy: potions, charms, keys

    #If character is goblin
        #Can buy: bow and arrow, potions, charms, keys
store_items = {
    "human": {"sword": 30, "potions": 10, "charms": 15, "keys": 5},
    "dog": {"potions": 10, "charms": 15, "keys": 5},
    "bear": {"potions": 10, "charms": 15, "keys": 5},
    "goblin": {"bow and arrow": 25, "potions": 10, "charms": 15, "keys": 5}
}

# run inventory
inventory_menu()