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