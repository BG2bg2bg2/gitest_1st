human_strength = 23
human_health = 50
dog_strength = 47
dog_health = 120
goblin_strength = 35
goblin_health = 100
bear_strength = 12
bear_health = 25 

sword = 10
potions = 20
charms = 10
keys = 50
bow = 10
arrow = 10


#Create inventory list
inventory = []
#Create gold amount for user
gold = 100
#Ask user to choose a character type
print("1. Human")
print("2. dog")
print("3. goblin")
print("4. bear")
character_type = input("Choose a Character Type:  ")
#Store character type
if character_type == "1":
    print(f"strength = {human_strength}, health = {human_health}")
if character_type == "2":
    print(f"strength = {dog_strength}, health = {dog_health}")
if character_type == "3":
    print(f"strength = {goblin_strength}, health = {goblin_health}")
if character_type == "4":
    print(f"strength = {bear_strength}, health = {bear_health}")
#Function inventory_menu
    #Ask user:
        #1. Store item
        #2. Change item
        #3. Quit inventory
def inventory_menu():
    print("1. Store Item")
    print("2. Change Item")
    print("3. Quit inventory")
    print("4. View Inventory")
    menu = input("What do you want to do?: ")
    #If user chooses store item
        #Ask: collect or buy?
    if menu == "1":
        store_item = input("Do you want to collect or buy an item: ")
        #If collect
            #Ask for item name
            #Add item to inventory
        if store_item == "collect":
            collect = input("What item do you want to collect: ")
            inventory.append(collect)
            print(inventory)
        #If buy
        #Show items allowed for the user's character type
        if store_item == "buy":
            if character_type == "1":
                print("You can buy sword, potions, charms, and keys ")
            if character_type == "2":
                print("you can buy potions, charms, and keys")
            if character_type == "3":
                print("you can buy bow and arrow, potions, charms, and keys")
            if character_type == "4":
                print("You can buy potions, charms, and keys ")
            buy = input("What item do you want to buy: ")
            cost 
            
            inventory.append(buy)
            print(inventory)



            
            #Ask which item to buy
            #Check if user has enough gold
            #If yes
                #Remove gold
                #Add item to inventory
            #Else
                #Show error message

    #If user chooses change item
        #Ask:
            #1. Set soul free
            #2. Use or drop item

        #If set soul free
            #Show souls in inventory
            #Ask which soul to free
            #Remove soul from inventory

        #If use or drop item
            #Ask which item
            #Use or remove item from inventory

    #If user chooses quit
        #Exit inventory and return to game
inventory_menu()
#Character rules:
    #If character is human
        #Can buy: sword, potions, charms, keys

    #If character is dog or bear
        #Can use abilities: bite, run faster
        #Can buy: potions, charms, keys

    #If character is goblin
        #Can buy: bow and arrow, potions, charms, keys
