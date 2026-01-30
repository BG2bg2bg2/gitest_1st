#Hi

import random

#skills = []
skills = []

#souls
souls = 0
#level = 1
level = 1
# leveling up function
def function():
    #if user has collected 3  of souls then
    if souls == 3:
    # you have leveled up by one level 1 += level 
        level += 1
    #while level < 10 
    while level < 10:
    # keep adding a level for every three kills
      level += 1 
        

# making a function to view characters options and what skills they have
def characters_options():
#   storing all the characterics for each character in an induval list
#   human = [ strength = 23, health = 50 ]
#   dog = [ strength = 47 ,health= 120,]
#   goblin  = [strength = 35 ,health= 100, ]
#   bear = [strength = 12 ,health = 25 ,]
    human = {"strength": 23, "health": 50}
    dog = {"strength": 47, "health": 120}
    goblin = {"strength": 35, "health": 100}
    bear = {"strength": 12, "health": 25}


# making a function to handle skill dependencies and prerequisites(by using if statements)
def skill_change():
# list for special skills [flying monkey, flying dog,spin kick]
  special_skills = ["flying monkey", "flying dog","spin kick,flying blobfish"]
    # if user had 10 == souls
  if souls == 10: 
    #   show user you have unlocked special skill
    print("you have unlocked a special skills")
    #   pull one of the random skills from the list
    random_skill = random.choice(special_skills)
    #add it onto the skills
    skills.append(random_skill)
  # else if user had eqaul 8 souls
  elif souls == 8:
        #show user you got a special skill
        print("you got a special skills")
        # its flying blobfish 
        print("ITS FLYING BLOBFISH")
        # add blobfish to SKILL LIST
        skills.append("flying blobfish")

    # elif user had 5 == souls
  elif souls == 5:
    #    how user you dont get a skill
    print("you dont get a skill")
    #else print you just moved up a level
  else:
     print("you don't get anything")
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

# Ask user to choose a character type
#Store character type
character = input("choose character(human, dog, bear, goblin): ")

def view_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(f"- {item}")
    print(f"Total Gold: {gold}")

# Function inventory_menu
  #Ask user:
        #1. Store item
        #2. Change item
        #3. Quit inventory
def inventory_menu():
    global gold

    while True:
        print("1. store item")
        print("2. change item")
        print("3. view inventory") 
        print("4. quit inventory")

        choice = input("choose: ")

        # If user chooses store item
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
                print(f" {item} added to the inventory")
                
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

        # If user chooses change item
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
        #Exit inventory and return to game

        elif choice == "4":
            print("leaving inventory")
            break
        
        else:
            print("Invalid option")

# run inventory
inventory_menu()