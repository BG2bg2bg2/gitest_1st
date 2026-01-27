#Hi



#Create inventory dictionary
#Create gold amount for user

#Ask user to choose a character type
#Store character type

#Function inventory_menu
    #Ask user:
        #1. Store item
        #2. Change item
        #3. Quit inventory

    #If user chooses store item
        #Ask: collect or buy?

        #If collect
            #Ask for item name
            #Add item to inventory

        #If buy
            #Show items allowed for the user's character type
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

#Character rules:
    #If character is human
        #Can buy: sword, potions, charms, keys

    #If character is dog or bear
        #Can use abilities: bite, run faster
        #Can buy: potions, charms, keys

    #If character is goblin
        #Can buy: bow and arrow, potions, charms, keys
