#main menu
#options user has

#global variables
i = 1
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
    'cloths': {
        'shirts': {
            'red shirt': {'type': 'shirt', 'price': 20},
            'flag shirt': {'type': 'shirt', 'price': 33},
        },
        'pants': {
            'blue shorts': {'type': 'pants', 'price': 10},
            'jeans': {'type': 'pants', 'price': 25},
        }
    }
}
body_type = "human"

def get_shop_items():
    #Return a flat list of (name, info, category).
    items = []
    for category, sub_dict in shop.items():
        if category == 'bodies':
            for name, info in sub_dict.items():
                items.append((name, info, 'bodies'))
        elif category == 'cloths':
            for sub_cat, sub_items in sub_dict.items():
                for name, info in sub_items.items():
                    items.append((name, info, sub_cat))  # category as sub_cat like 'shirts'
    return items


def find_in_shop(name):
    #Return (info, category) if name exists in shop, else (None, None)
    for category, sub_dict in shop.items():
        if category == 'bodies':
            if name in sub_dict:
                return sub_dict[name], 'bodies'
        elif category == 'cloths':
            for sub_cat, sub_items in sub_dict.items():
                if name in sub_items:
                    return sub_items[name], sub_cat
    return None, None

#funtion for main menu
def main():
    #ask the user for the following
    print("\n1 is to change your character")
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
    #do you want to go through a tutorial (totor)
    elif choice == '3':
        #call storage
        #call tutorial
        totor()
    #do you want to know the ranks of everything around you? (seek)
    elif choice == '4':
        #call seek
        seek()
    elif choice == '5':
        shop_menu()
    else:
        print("\nInvalid choice. Please enter a number from 1 to 5.")
        main()

def closet():
    #check if there is stuff in inventory
    #if there is cloths in inventory
    if len(invent) > 0:
        print("\nThese are the items in your inventory:")
        for index, item in enumerate(invent):
            print(f"{index + 1}. {item}")
        choice = input("\nEnter the number of the item you want to wear, or 'q' to quit: ")
        if choice.lower() == 'q':
            return
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(invent):
                selected_item = invent[choice_index]
                item_info, category = find_in_shop(selected_item)
                if item_info:
                    cloths[category] = selected_item
                    print(f"\nYou are now wearing the {selected_item}.")
                else:
                    print("\nItem not found in shop data.")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")
    else:
        print("you can't change your character because you have no items in your inventory.")
    main()

def storage():
    #check if there is stuff in inventory
    if len(invent) > 0:
        print("These are the items in your inventory:")
        for item in invent:
            print(f"- {item}")
    else:
        print("Your inventory is empty.")
    main()

def totor():
    print("Welcome to the tutorial!")
    #display what pweres do you want to learn about
    #display powers you have
    print("You have the following powers:")
    for power in powers:
        print(f"- {power}")
    print("Each power allows you to perform different actions in the game.")
    #display how to use each power
    for index, power in enumerate(powers):
        print(f"{index + 1}. {power}")
    print("To use a power, you go through the compat situation and each one gives you ability to help go through each room  .")
    main()
    #display index in enumorate skills
    #dislpay index + 1 and skill
    for index, skill in enumerate(skills):
        print(f"{index + 1}. {skill}")
        #display how to use each skill
    print("Skills are special abilities that you can unlock as you progress in the game and level up.")
def seek():
    print("Current Ranks:")
    for name, info in rank.items():
        print(f"{name.capitalize()}: Level {info['level']}")
    main()
def shop_menu():
    global gold
    print(f"You have {gold} gold.")
    items = get_shop_items()
    print("Items available in the shop:")
    for index, (name, info, category) in enumerate(items):
        print(f"{index + 1}. {name} ({category}) - {info['price']} gold")
    choice = input("\nEnter the number of the item you want to buy, or 'q' to quit: ")
    if choice.lower() == 'q':
        main()
        return
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(items): 
            selected_name, selected_info,  selected_category = items[choice_index]
            if gold >= selected_info['price']:
                gold -= selected_info['price']
                invent.append(selected_name)
                print(f"You bought a {selected_name} for {selected_info['price']} gold.")
            else:
                print("You don't have enough gold to buy that item.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
    shop_menu()

main()
