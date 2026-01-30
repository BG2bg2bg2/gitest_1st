# Create inventory list
# Create gold amount for user
inventory = []
gold = 50

store_items = {
    "human": {"sword": 30, "potions": 10, "charms": 15, "keys": 5},
    "dog": {"potions": 10, "charms": 15, "keys": 5},
    "bear": {"potions": 10, "charms": 15, "keys": 5},
    "goblin": {"bow and arrow": 25, "potions": 10, "charms": 15, "keys": 5}
}

# Ask user to choose a character type
character = input("choose character (human, dog, bear, goblin): ")

# NEW FUNCTION: View Inventory
def view_inventory():
    print("\n--- YOUR INVENTORY ---")
    if not inventory:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")
    print(f"Total Gold: {gold}")

# Function inventory_menu
def inventory_menu():
    global gold

    while True:
        print("\n1. store item")
        print("2. change item")
        print("3. view inventory") # Added this option
        print("4. quit inventory")

        choice = input("choose: ")

        # If user chooses store item
        if choice == "1":
            method = input("collect or buy? ")
            if method == "collect":
                item = input("item name: ")
                inventory.append(item)
                print(f" {item} added to the inventory")
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

        # If user chooses change item
        elif choice == "2":
            print("1. set soul free")
            print("2. use or drop item")
            change = input("choose: ")
            
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
            
            elif change == "2":
                print("inventory:", inventory)
                item = input("which item? ")
                if item in inventory:
                    action = input("use or drop? ")
                    if action == "use":
                        print("you used", item)
                    elif action == "drop":
                        inventory.remove(item)
                        print(item, "dropped")
                else:
                    print("item not found")

        # If user chooses view inventory
        elif choice == "3":
            view_inventory()

        # If user chooses quit
        elif choice == "4":
            print("leaving inventory")
            break
        
        else:
            print("Invalid option")

# run inventory
inventory_menu()
