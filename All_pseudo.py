#START PROGRAM
#def main menu 
def main():
  while True:
    try:
      print("1. Make Character")
      print("2. Store")
      print("3. Inventory")
      print("4. View Stats")
      print("5. Apply Power-Ups")
      print("6. Check Level Up")
      print("7. Exit")
      choice = input("Choice: ").strip()
    except (EOFError, KeyboardInterrupt):
      print("\nExiting.")
      break
    if choice == "1":
      start_game()
    elif choice == "2":
      store_menu()
    elif choice == "3":
      inventory_menu()
    elif choice == "4":
      display_stats()
    elif choice == "5":
      apply_powerups()
    elif choice == "6":
      check_level_up()
    elif choice == "7":
      break
    else:
      print("Invalid choice")

#DATA SETUP
#SET level = 1
SET_level = 1
#SET rank = "Novice"
SET_rank = "Novice"
#SET money = 100
SET_money = 100
#SET souls = 0
SET_souls = 0

#// Attributes list
#// Index: 0 = Strength, 1 = Intelligence, 2 = Speed, 3 = Health
#SET attributes = [10, 8, 6, 100]
SET_attributes = [10, 8, 6, 100]

# Inventory list
Inventory = []

#// Store inventory
#SET store = {
#    "Sword": 50,
#    "Potion": 10,
#    "Charm": 20,
#    "Key": 30
SET_store = {
  "Sword": 50,
  "Potion": 10,
  "Charm": 20,
  "Key": 30
}

#// Power-ups list
#SET powerUps = empty list
SET_powerups = []

# extra: skills list to record special skills unlocked on level up
SET_skills = []

# Character details (keep qualities & height accessible)
SET_character = {
  "type": "Unknown",
  "skin": "Unknown",
  "eyes": "Unknown",
  "height": "Unknown",
  "hunter": "Unknown"
}

#CHARACTER CREATION FUNCTION

#FUNCTION startGame()
#    DISPLAY "Choose a character type: Human, Dog, Goblin, Bear"
#    INPUT characterType
#
#    DISPLAY "Choose skin/fur color:"
#    INPUT skinColor
#
#    DISPLAY "Choose eye color:"
#    INPUT eyeColor
#
#    DISPLAY "Choose height:"
#    INPUT height
#
#    DISPLAY "Choose hunter type:"
#    INPUT hunterType
#
#    UPDATE stats based on characterType
#
#    DISPLAY "Character created!"
#END FUNCTION

def start_game():
  global SET_attributes, SET_rank, SET_character
  print("# Character Creation (pseudocode preserved above)")

  valid_types = {"human", "dog", "goblin", "bear"}
  while True:
    char_type_in = input("Choose a character type (Human, Dog, Goblin, Bear): ").strip()
    if not char_type_in:
      print("Please enter a character type.")
      continue
    char_type = char_type_in.title()
    if char_type.lower() in valid_types:
      break
    print("Invalid type. Choose one of:", ", ".join(t.title() for t in valid_types))

  # simple validation for short text qualities; allow freeform but ensure non-empty
  def ask_nonempty(prompt, default="Unknown"):
    while True:
      v = input(prompt).strip()
      if v:
        return v
      print("Please enter a value (cannot be empty).")

  skin = ask_nonempty("Choose skin/fur color: ")
  eyes = ask_nonempty("Choose eye color: ")
  # height: accept number or text but require input
  height = ask_nonempty("Choose height (e.g. 180cm, 5'11\"): ")
  hunter = ask_nonempty("Choose hunter type: ")

  # Update stats based on characterType
  if char_type == "Human":
    SET_attributes = [10, 9, 7, 100]
    SET_rank = "Human Novice"
  elif char_type == "Dog":
    SET_attributes = [8, 6, 12, 90]
    SET_rank = "Canine Scout"
  elif char_type == "Goblin":
    SET_attributes = [12, 6, 8, 85]
    SET_rank = "Goblin Grunt"
  elif char_type == "Bear":
    SET_attributes = [15, 5, 5, 130]
    SET_rank = "Bear Brute"
  else:
    print("Unknown type, defaulting to Human.")
    SET_attributes = [10, 8, 6, 100]
    SET_rank = "Novice"

  # store character qualities for viewing later
  SET_character["type"] = char_type
  SET_character["skin"] = skin
  SET_character["eyes"] = eyes
  SET_character["height"] = height
  SET_character["hunter"] = hunter

  print("Character created!")
  print(f"Type: {char_type}, Skin: {skin}, Eyes: {eyes}, Height: {height}, Hunter: {hunter}")
  print(f"Stats: Strength={SET_attributes[0]}, Intelligence={SET_attributes[1]}, Speed={SET_attributes[2]}, Health={SET_attributes[3]}")
  print(f"Rank set to: {SET_rank}")

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

def display_stats():
  print("# Display Stats (pseudocode preserved above)")
  print(f"Level: {SET_level}")
  print(f"Rank: {SET_rank}")
  print(f"Souls: {SET_souls}")
  print(f"Strength: {SET_attributes[0]}")
  print(f"Intelligence: {SET_attributes[1]}")
  print(f"Speed: {SET_attributes[2]}")
  print(f"Health: {SET_attributes[3]}")
  # Show character qualities & height
  print("Character Type:", SET_character.get("type", "Unknown"))
  print("Skin/Fur Color:", SET_character.get("skin", "Unknown"))
  print("Eye Color:", SET_character.get("eyes", "Unknown"))
  print("Height:", SET_character.get("height", "Unknown"))
  print("Hunter Type:", SET_character.get("hunter", "Unknown"))
  if SET_skills:
    print("Skills:", ", ".join(SET_skills))

#INVENTORY FUNCTION

#FUNCTION inventoryMenu()
#   WHILE true
#       DISPLAY "1. View Inventory"
#       DISPLAY "2. Use or Drop Item"
#       DISPLAY "3. Set a Soul Free"
#       DISPLAY "4. Exit Inventory"
#       INPUT choice
#
#       IF choice == 1 THEN
#           DISPLAY inventory
#
#       ELSE IF choice == 2 THEN
#           INPUT itemName
#           REMOVE or USE item from inventory
#
#       ELSE IF choice == 3 THEN
#           IF souls > 0 THEN
#             souls = souls - 1
#             DISPLAY "You set a soul free."
#         ELSE
#             DISPLAY "No souls to free."
#       END IF
#
#        ELSE IF choice == 4 THEN
#           BREAK LOOP
#    END IF
#   END WHILE
#END FUNCTION

def inventory_menu():
  global Inventory, SET_souls, SET_attributes
  while True:
    print("# Inventory Menu (pseudocode preserved above)")
    print("1. View Inventory")
    print("2. Use or Drop Item")
    print("3. Set a Soul Free")
    print("4. Exit Inventory")
    choice = input("Choice: ").strip()
    if choice == "1":
      if not Inventory:
        print("Inventory: Empty")
      else:
        for i, it in enumerate(Inventory, 1):
          print(f"{i}. {it}")
    elif choice == "2":
      if not Inventory:
        print("Inventory empty.")
        continue
      # show indexed list and allow numeric or name selection
      for i, it in enumerate(Inventory, 1):
        print(f"{i}. {it}")
      sel = input("Enter item number or name to use/drop: ").strip()
      if not sel:
        print("No selection made.")
        continue
      # try number
      item = None
      if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(Inventory):
          item = Inventory[idx]
        else:
          print("Invalid item number.")
          continue
      else:
        # case-insensitive match by name
        lowered = sel.lower()
        for it in Inventory:
          if it.lower() == lowered:
            item = it
            break
        if item is None:
          print("Item not found.")
          continue

      # Simple use behavior: potion heals, sword increases strength temporarily, others drop
      if item.lower() == "potion":
        SET_attributes[3] += 20
        print("You used a Potion. Health increased by 20.")
      elif item.lower() == "sword":
        SET_attributes[0] += 2
        print("You equipped a Sword. Strength increased by 2.")
      else:
        print(f"You dropped {item}.")
      # remove the item (first occurrence)
      try:
        Inventory.remove(item)
      except ValueError:
        pass

    elif choice == "3":
      if SET_souls > 0:
        SET_souls -= 1
        print("You set a soul free.")
      else:
        print("No souls to free.")
    elif choice == "4":
      break
    else:
      print("Invalid choice.")

#STORE FUNCTION

#FUNCTION storeMenu()
#    WHILE true
#        DISPLAY "Money: " + money
#        DISPLAY store
#        DISPLAY "Choose an item to buy or type EXIT"
#        INPUT itemChoice
#
#        IF itemChoice == "EXIT" THEN
#          BREAK LOOP
#
#        ELSE IF store[itemChoice] > money THEN
#          DISPLAY "Too much for too little money."
#
#        ELSE IF store[itemChoice] <= money THEN
#          money = money - store[itemChoice]
#          ADD itemChoice to inventory
#          REMOVE itemChoice from store
#          DISPLAY "Item purchased!"
#        ELSE
#          DISPLAY "Enter a valid item."
#    END WHILE
#END FUNCTION

def store_menu():
  global SET_money, Inventory, SET_store
  while True:
    print("# Store Menu (pseudocode preserved above)")
    print(f"Money: {SET_money}")
    if not SET_store:
      print("Store is empty.")
      break
    for item, price in SET_store.items():
      print(f"{item}: {price}")
    choice = input("Choose an item to buy or type EXIT: ").strip()
    if not choice:
      print("Enter a valid item or EXIT.")
      continue
    if choice.upper() == "EXIT":
      break
    # case-insensitive lookup
    chosen_key = None
    for key in list(SET_store.keys()):
      if key.lower() == choice.lower():
        chosen_key = key
        break
    if chosen_key is None:
      print("Enter a valid item.")
      continue
    price = SET_store[chosen_key]
    if price > SET_money:
      print("Too much for too little money.")
    else:
      SET_money -= price
      Inventory.append(chosen_key)
      # Remove item from store to match pseudocode's "REMOVE itemChoice from store"
      SET_store.pop(chosen_key, None)
      print("Item purchased!")

# POWER-UP FUNCTION

#FUNCTION applyPowerUps()
#   FOR each powerUp in powerUps
#       SET statType = powerUp.statType
#       SET amount = powerUp.amount
#
#       IF statType == "strength" THEN
#           attributes[0] = attributes[0] + amount
#       ELSE IF statType == "intelligence" THEN
#           attributes[1] = attributes[1] + amount
#       ELSE IF statType == "speed" THEN
#           attributes[2] = attributes[2] + amount
#       ELSE IF statType == "health" THEN
#           attributes[3] = attributes[3] + amount
#       END IF
#   END FOR
#
#   CLEAR powerUps
#END FUNCTION

def apply_powerups():
  global SET_powerups, SET_attributes
  print("# Apply Power-Ups (pseudocode preserved above)")
  if not SET_powerups:
    print("No power-ups to apply.")
    return
  for pu in SET_powerups:
    stat = pu.get("statType", "").lower()
    amt = pu.get("amount", 0)
    if stat == "strength":
      SET_attributes[0] += amt
    elif stat == "intelligence":
      SET_attributes[1] += amt
    elif stat == "speed":
      SET_attributes[2] += amt
    elif stat == "health":
      SET_attributes[3] += amt
  SET_powerups = []
  print("Power-ups applied.")

#/LEVEL UP FUNCTION

#FUNCTION checkLevelUp()
#    WHILE souls >= 10
#      level = level + 1
#      souls = souls - 10
#      DISPLAY "You leveled up!"
#
#      IF souls >= 10 THEN
#          DISPLAY "You unlocked a special skill!"
#          ADD "Special Skill" to attributes
#      ELSE IF souls >= 5 THEN
#          DISPLAY "No new skill this level."
#      ELSE
#          DISPLAY "You moved up a level."
#      END IF
#    END WHILE
#END FUNCTION

def check_level_up():
  global SET_souls, SET_level, SET_skills
  print("# Check Level Up (pseudocode preserved above)")
  leveled = False
  while SET_souls >= 10:
    SET_level += 1
    SET_souls -= 10
    leveled = True
    print("You leveled up!")
    if SET_souls >= 10:
      print("You unlocked a special skill!")
      SET_skills.append(f"Special Skill L{SET_level}")
    elif SET_souls >= 5:
      print("No new skill this level.")
    else:
      print("You moved up a level.")
  if not leveled:
    print("Not enough souls to level up.")

#MAIN MENU

#CALL startGame()

#WHILE true
#    DISPLAY "1. View Stats"
#    DISPLAY "2. Inventory"
#    DISPLAY "3. Store"
#    DISPLAY "4. Apply Power-Ups"
#    DISPLAY "5. Exit Game"
#END PROGRAM

if __name__ == "__main__":
  main()
