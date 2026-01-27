#main menu
#options user has

#funtion for main menu
    #ask the user for the following
    #do you want to change your character (closet)
        #call closet
    #do you want to see what is in your inventory (storage)
        #call storage
    #do you want to go through a toltorial to get to know your powers? (totorial)
        #call totorial
    #do you want to know the ranks of everything around you? (seek)
        #call seek
    #do you want to buy items from the shop? (shop)
        #call shop


#funtion for closet
    #display cloths in the closet
    #display types of bodies in closet (like human, bear, goblin, wolf, ex)
    #ask user if they want to change cloths or body
    #if cloths or body are in closet
    #ask if they want to put it on
    #else if cloths or body not in closet but if shop
        #dislpay it is in shop for $...
    #else display not able to be found or does not exist

#funtion for storage
    #if inventory has items
        #dislplay inventory
    #else display there are no items in your inventory

#funtion for totorial
    #dislplay powers that user has
    #ask if they want to do a quick totorial on a specific power they have
    #if the number they input is a power the have display how to use it step by step
    #else if the number they input is not a power they have
        #display it is in a later level or does not exist

#funtion for seek
    #display levels and ranks everyhting/one is at
    #display each thing is at a level that _ higher or _lower than you

#funtion for shop
    #display every item and body in the shop and the price each is at
    #if user wants to buy one subtract user money from item money
        #if item is too much 
            #dislpay you can't get into debt
        #else if item is enough do math
    #else if user wants to leave
        #continue the program
    #else
        #display enter a valid input