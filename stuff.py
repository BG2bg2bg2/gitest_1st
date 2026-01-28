#START PROGRAM
#def main menu 
def main():
    while True:
        print("1.Make Character")
        print("2.Store")
        print("3. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            
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

