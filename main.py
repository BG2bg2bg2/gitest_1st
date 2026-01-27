#START PROGRAM

#1. Store character attributes in a list
# Index: 0 = Strength, 1 = Intelligence, 2 = Speed, 3 = Health
#SET attributes = [10, 8, 6, 100]
#2. Store collected power-ups in a list
#SET powerUps = empty list

#3. Function: Display attributes
#FUNCTION displayAttributes()
#    PRINT "Character Attributes:"
#    PRINT "Strength: " + attributes[0]
 #   PRINT "Intelligence: " + attributes[1]
  ## PRINT "Health: " + attributes[3]
#END FUNCTION

#5. Function: Apply all power-ups to attributes
#FUNCTION applyPowerUps()
#    FOR each powerUp in powerUps
#        SET name = powerUp.name
#        SET statType = powerUp.statType
  #      SET amount = powerUp.amount
#
  #      IF statType == "strength" THEN
 #           attributes[0] = attributes[0] + amount
 #       ELSE IF statType == "intelligence" THEN
 #           attributes[1] = attributes[1] + amount
 #       ELSE IF statType == "speed" THEN
  #          attributes[2] = attributes[2] + amount
 #       ELSE IF statType == "health" THEN
  #          attributes[3] = attributes[3] + amount
   #     END IF
#
 #       PRINT "Applied " + name + ": " + statType + " +" + amount
  #  END FOR

 #   CLEAR powerUps   
 # remove used power-ups
#END FUNCTION

# 6. Main loop for inventory + attributes
#WHILE true
#    PRINT "1. View Attributes"
 #   PRINT "2. Add Power-Up"
 #   PRINT "3. Use Power-Ups"
 #   PRINT "4. Exit"

 #   INPUT choice

 #   IF choice == 1 THEN
  #      CALL displayAttributes()

   # ELSE IF choice == 2 THEN
    #    INPUT powerUpName
     #   INPUT statType
      #  INPUT amount
       # CALL addPowerUp(powerUpName, statType, amount)

#    ELSE IF choice == 3 THEN
 #       CALL applyPowerUps()

#    ELSE IF choice == 4 THEN
#        PRINT "Exiting game..."
#        BREAK LOOP
#    END IF
#END WHILE

#END PROGRAM
