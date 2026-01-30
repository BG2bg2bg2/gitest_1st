#main menu
#options user has

#global variables
rank = {
    "you":{'level': 1},
    'enemy':{'level': 10}
}
selfs = {}
cloths = {}
stuff = []
invent = []
skills = []
powers = ["fly", "run", "seek"]
gold = 50
shop = {
    'bodies': {
        'human': {'type': 'form', 'price': 22},
        'bear': {'type': 'form', 'price': 25},
        'goblin': {'type': 'form', 'price': 18},
        'wolf': {'type': 'form', 'price': 22},
    },
    'shirts': {
        'red shirt': {'type': 'shirt', 'price': 20},
        'flag shirt': {'type': 'shirt', 'price': 33},
    },
    'pants': {
        'blue shorts': {'type': 'pants', 'price': 10},
    },
}   
body_type = "human"

def get_shop_items():
    #Return a flat list of (name, info, category).
    items = []
    for category, items_dict in shop.items():
        for name, info in items_dict.items():
            items.append((name, info, category))
    return items


def find_in_shop(name):
    #Return (info, category) if name exists in shop, else (None, None)
    for category, items_dict in shop.items():
        if name in items_dict:
            return items_dict[name], category
    return None, None

#funtion for main menu
def main():
    #ask the user for the following
    print("1 is to change your character")
    print("2 is to look through inventory")
    print("3 is to go through a quick tutorial")
    print("4 is to see the ranks of everyone")
    print("5 is to look/buy items in the shop")
    print("enter a number 1 - 5")
    choice = input("What do you want to do?: ")
    #do you want to change your character (closet)
    if choice == '1':
        #call closet
        closet()
    #do you want to see what is in your inventory (storage)
    elif choice == '2':
        #call storage
        storage()
    #do you want to go through a toltorial to get to know your powers? (totorial)
    elif choice == '3':
        #call tutorial
        totor()
    #do you want to know the ranks of everything around you? (seek)
    elif choice == '4':
        #call seek
        seek()
    #do you want to buy items from the shop? (shop)
    elif choice == '5':
        #call shop
        shopping()

#funtion for closet
def closet():
    global body_type
    #display cloths in the closet
    print("clothes:", cloths)
    #display types of bodies in closet (like human, bear, goblin, wolf, ex)
    print("body type:", body_type)
    #ask user if they want to change cloths or body
    ask = input("enter a number 1 - 3\n1 is to change cloths\n2 is to change your physical form\n3 is to do a diffrent option: ")
    #if cloths or body are in closet
    if ask == '1':
        #ask if they want to put it on
        what = input("What do you want to put on? ")
        if what in cloths:
            selfs[what] = cloths[what]
            print(f"You have put on {what}")
        else:
            info, category = find_in_shop(what)
            if info:
                #display it is in shop for $...
                print(f"{what} is in the shop for {info['price']} gold ({category}).")
                #ask user if they want to get that item
                check = input("Do you want to go shopping for that item? (Y/N)").lower()
                if check == "y":
                    #call shopping
                    shopping()
                else:
                    print("Okay, item not purchased.")
            else:
                #else display not able to be found or does not exist
                print("Can't find the item that you are wanting")
    elif ask == '2':
        #change physical form
        bodies = shop.get('bodies', {})
        print("Available bodies:")
        for b in bodies:
            print(f"- {b} ({bodies[b]['price']} gold)")
        pick = input("Enter the body you want to switch to (or press Enter to cancel): ")
        if not pick:
            return
        if pick in bodies:
            body_type = pick
            print(f"You changed your body type to {body_type}.")
        else:
            print("That body is not available.")
            
    
        
    

#funtion for storage
def storage():
    #if inventory has items
    if invent:
        #dislplay inventory
        print(invent)
    #else display there are no items in your inventory
    else:
        print("no items in inventory")

#funtion for totorial
def totor():
    #dislplay powers that user has
    print(powers)
    #ask if they want to do a quick totorial on a specific power they have
    do = input("do you want to go through a quick totorial to learn how to use your powers? (Y/N): ").lower()
    if do == "y":
        for i, p in enumerate(powers, start=1):
            print(f"{i}. {p}")
        choice = input("Enter the number of the power to learn about (or press Enter to return): ")
        if not choice:
            return
        try:
            idx = int(choice) - 1
            power = powers[idx]
            if power == 'fly':
                print("Fly: Press F to take off. Hold to float.")
            elif power == 'run':
                print("Run: Press R to sprint for short bursts.")
            elif power == 'seek':
                print("Seek: Use to reveal nearby ranks.")
            else:
                print(f"No tutorial for {power}.")
        except (ValueError, IndexError):
            print("Invalid selection.")
    #if the number they input is a power the have display how to use it step by step
    #else if the number they input is not a power they have
        #display it is in a later level or does not exist

#funtion for seek
def seek():
    #display levels and ranks everyhting/one is at and the diffrence between you and them
    print(f"Enemy is at level {rank['enemy']['level']}")
    #display your level and the difference versus the enemy
    you_level = rank['you']['level']
    enemy_level = rank['enemy']['level']
    diff = you_level - enemy_level
    if diff == 0:
        print(f"Your rank is at level {you_level} (the same as the enemy).")
    elif diff > 0:
        print(f"Your rank is at level {you_level} ({diff} level(s) higher than the enemy).")
    else:
        print(f"Your rank is at level {you_level} ({abs(diff)} level(s) lower than the enemy).")
#funtion for shop
def shopping():
    global gold
    #display every item and body in the shop and the price each is at
    print(shop)
    #ask user if they want to buy something
    ask = input("do you want to buy an item? (Y/N)").lower()
    #if ask is yes as y
    if ask == "y":
        #show available items with prices
        print(f"You have {gold} gold.")
        items = get_shop_items()  # returns list of (name, info, category)
        items_map = {}
        for idx, (name, info, category) in enumerate(items, start=1):
            print(f"{idx}. {name} ({category}) - {info.get('price',0)} gold")
            items_map[idx] = (name, info, category)

        choice = input("Enter item number (or press Enter to cancel): ")
        if not choice:
            return
        try:
            num = int(choice)
            if num in items_map:
                name, info, category = items_map[num]
                # proceed to buy/equip: price = info['price']
            else:
                print("Invalid number.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

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
#START PROGRAM
#def main menu 
def main():
    while True:
        print("1.Make Character")
        print("2.Store")
        print("3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            charact()    
        elif choice == "2":
            break
    #    Otherwise: print "Invalid choice"
        else:
            print("Invalid choice")
#DATA SETUP
#SET level = 1
SET_level = 1
#SET rank = "Novice"
SET_rank = "Novice"
#SET money = 100
SET_money = 100

#// Attributes list
#// Index: 0 = Strength, 1 = Intelligence, 2 = Speed, 3 = Health
#SET attributes = [10, 8, 6, 100]
Strength = 0,Intelligence = 0, Speed = 0,Health = 0
Inventory = []
#// Inventory dictionary
#SET inventory = empty dictionary
SEt_Inventory = []
#// Store inventory
#SET store = {
#    "Sword": 50,
#    "Potion": 10,
#    "Charm": 20,
#    "Key": 30
#}

SET_store = {
    "Sword": 50,
    "Potion": 10,
    "Charm": 20,
    "Key": 30
}
    

#// Power-ups list
#SET powerUps = empty list
SET_powerups = []

#CHARACTER CREATION FUNCTION

#FUNCTION startGame()
#    DISPLAY "Choose a character type: Human, Dog, Goblin, Bear"
 #   INPUT characterType

#    DISPLAY "Choose skin/fur color:"
#    INPUT skinColor

#    DISPLAY "Choose eye color:"
#    INPUT eyeColor

#    DISPLAY "Choose height:"
#    INPUT height

#    DISPLAY "Choose hunter type:"
#    INPUT hunterType

#    UPDATE stats based on characterType

#    DISPLAY "Character created!"
#END FUNCTION

def start_game():
#    DISPLAY "Choose a character type: Human, Dog, Goblin, Bear"
 #   INPUT characterType

#    DISPLAY "Choose skin/fur color:"
#    INPUT skinColor

#    DISPLAY "Choose eye color:"
#    INPUT eyeColor

#    DISPLAY "Choose height:"
#    INPUT height

#    DISPLAY "Choose hunter type:"
#    INPUT hunterType

#    UPDATE stats based on characterType

#    DISPLAY "Character created!"
#END FUNCTION


#/DISPLAY STATS FUNCTION

#FUNCTION displayStats()
#    DISPLAY "Level: " + level
#    DISPLAY "Rank: " + rank
#    DISPLAY "Souls: " + souls
#    DISPLAY "Strength: " + attributes[0]
#    DISPLAY "Intelligence: " + attributes[1]
#    DISPLAY "Speed: " + attributes[2]
#    DISPLAY "Health: " + attributes[3]
#END FUNCTION


#INVENTORY FUNCTION

#FUNCTION inventoryMenu()
   # WHILE true
    #    DISPLAY "1. View Inventory"
    #    DISPLAY "2. Use or Drop Item"
    #    DISPLAY "3. Set a Soul Free"
    #    DISPLAY "4. Exit Inventory"
   #     INPUT choice

  #      IF choice == 1 THEN
   #         DISPLAY inventory

   #     ELSE IF choice == 2 THEN
   #         INPUT itemName
   #         REMOVE or USE item from inventory

   #     ELSE IF choice == 3 THEN
   #         IF souls > 0 THEN
     #           souls = souls - 1
      #          DISPLAY "You set a soul free."
      #      ELSE
     #           DISPLAY "No souls to free."
        #    END IF

       # ELSE IF choice == 4 THEN
        #    BREAK LOOP
    #    END IF
#    END WHILE
#END FUNCTION


#STORE FUNCTION

#FUNCTION storeMenu()
#    WHILE true
#        DISPLAY "Money: " + money
#        DISPLAY store
#        DISPLAY "Choose an item to buy or type EXIT"
#        INPUT itemChoice

 #       IF itemChoice == "EXIT" THEN
       #     BREAK LOOP

    #    ELSE IF store[itemChoice] > money THEN
      #      DISPLAY "Too much for too little money."

   #     ELSE IF store[itemChoice] <= money THEN
    #        money = money - store[itemChoice]
     #       ADD itemChoice to inventory
     #       REMOVE itemChoice from store
      #      DISPLAY "Item purchased!"
     #   ELSE
       #     DISPLAY "Enter a valid item."
      #  END IF
   # END WHILE
#END FUNCTION

# POWER-UP FUNCTION

#FUNCTION applyPowerUps()
 #   FOR each powerUp in powerUps
   #     SET statType = powerUp.statType
     #   SET amount = powerUp.amount

     #   IF statType == "strength" THEN
      #      attributes[0] = attributes[0] + amount
     #   ELSE IF statType == "intelligence" THEN
      #      attributes[1] = attributes[1] + amount
     #   ELSE IF statType == "speed" THEN
      #      attributes[2] = attributes[2] + amount
     #   ELSE IF statType == "health" THEN
   #         attributes[3] = attributes[3] + amount
   #     END IF
  #  END FOR

#    CLEAR powerUps
#END FUNCTION


#/LEVEL UP FUNCTION

#FUNCTION checkLevelUp()
#    WHILE souls >= 10
  #      level = level + 1
 #       souls = souls - 10
 #       DISPLAY "You leveled up!"

 #       IF souls >= 10 THEN
 #           DISPLAY "You unlocked a special skill!"
  #          ADD "Special Skill" to attributes
  #      ELSE IF souls >= 5 THEN
  #          DISPLAY "No new skill this level."
  #      ELSE
  #          DISPLAY "You moved up a level."
 #       END IF
 #   END WHILE
#END FUNCTION


#MAIN MENU

#CALL startGame()

#WHILE true
#    DISPLAY "1. View Stats"
#    DISPLAY "2. Inventory"
#    DISPLAY "3. Store"
#    DISPLAY "4. Apply Power-Ups"
#    DISPLAY "5. Exit Game"
#    INPUT choice

#    IF choice == 1 THEN
  #      CALL displayStats()

#    ELSE IF choice == 2 THEN
  #      CALL inventoryMenu()

#    ELSE IF choice == 3 THEN
  #      CALL storeMenu()

#    ELSE IF choice == 4 THEN
  #      CALL applyPowerUps()

  #  ELSE IF choice == 5 THEN
    #    DISPLAY "Game Over"
    #    BREAK LOOP
 #   END IF

 #   CALL checkLevelUp()
#END WHILE

#END PROGRAM
  while True:
    main()