#main menu
#options user has

#global variables
selfs = {}
cloths = {}
stuff = []
invent = []
skills = []
powers = ["fly", "run", "seek"]
gold = 50
shop = {
    'human':{'type': 'form', 'price': 22,},
    'wolf':{"type": 'form', 'price': 22},
    "flag shirt":{'type': 'shirt', 'price': 33},
    'blue shorts': {'type': 'pants', "price": 10}
}
body_type = "human"
#funtion for main menu
def main():
    #ask the user for the following
    print("1 is to change your character")
    print("2 is to look through inventory")
    print("3 is to go through a quick tutorial")
    print("enter a number 1 - 4")
    choice = input("What do you want to do?")
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
        shop()

#funtion for closet
def closet():
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
        for _ in cloths(what):
            if what in cloths:
                selfs[what] = cloths[what]
                print(f"You have put on {what}")
            #else if cloths or body not in closet but if shop
            elif what in shop:
                #dislpay it is in shop for $...
                print(f"{what} is in the shop for {shop[what]["price"]} gold")
            else:
                #else display not able to be found or does not exist
                print("Can't find the item that you are wanting")
    
    
        
    

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
    do = input("do you want to go through a quick totorial to learn how to use your powers? (Y/N): ").lower
    if do == "y":
        for i in range(powers):
            print((1+1) + powers)
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
main()