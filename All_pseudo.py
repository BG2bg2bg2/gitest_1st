#START PROGRAM
#def main menu 
def main():
  while True:
    try:
      print("=================")
      print("1. Make Character")
      print("=================")
      print("2. Store")
      print("=================")
      print("3. Inventory")
      print("=================")
      print("4. View Stats")
      print("=================")
      print("5. Apply Power-Ups")
      print("=================")
      print("6. Check Level Up")
      print("=================")
      print("7. Exit")
      print("=================")
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
  print("# Character Creation")

  templates = {
    "human": ([10, 9, 7, 100], "Human Novice"),
    "dog": ([8, 6, 12, 90], "Canine Scout"),
    "goblin": ([12, 6, 8, 85], "Goblin Grunt"),
    "bear": ([15, 5, 5, 130], "Bear Brute"),
  }

  def ask_nonempty(prompt):
    while True:
      v = input(prompt).strip()
      if v:
        return v
      print("Please enter a value (cannot be empty).")

  def Ask_intger(prompt, min_value=0):
    while True:
      v = input(prompt).strip()
      try:
        n = int(v)
        if n < min_value:
          print(f"Enter a number >= {min_value}.")
          continue
        return n
      except ValueError:
        print("Enter a valid integer.")

  # choose type (allow custom)
  while True:
    print("Choose a character type: Human, Dog, Goblin, Bear, or type CUSTOM to make your own")
    char_type_in = input("Type: ").strip()
    if not char_type_in:
      print("Please enter a character type.")
      continue
    key = char_type_in.lower()
    if key in templates or key == "custom":
      break
    print("Invalid type. Choose one of:", ", ".join(t.title() for t in list(templates.keys()) + ["custom"]))

  if key == "custom":
    custom_name = ask_nonempty("Enter custom character type name: ").title()
    print("Now define base stats for your custom type.")
    Strength_value = Ask_intger("Strength (integer >=0): ", 0)
    Intelligence_Value = Ask_intger("Intelligence (integer >=0): ", 0)
    SPeed_valie = Ask_intger("Speed (integer >=0): ", 0)
    Health_Value = Ask_intger("Health (integer >=1): ", 1)
    rank_input = input("Optional: give a rank name for this type (leave blank for default): ").strip()
    rank_name = rank_input if rank_input else f"{custom_name} Novice"
    SET_attributes = [Strength_value, Intelligence_Value, SPeed_valie, Health_Value]
    SET_rank = rank_name
    char_type = custom_name
  else:
    vals, rank_name = templates[key]
    SET_attributes = vals.copy()
    SET_rank = rank_name
    char_type = key.title()

  # gather appearance / qualities
  skin = ask_nonempty("Choose skin/fur color: ")
  eyes = ask_nonempty("Choose eye color: ")
  height = ask_nonempty("Choose height (e.g. 180cm, 5'11\"): ")
  hunter = ask_nonempty("Choose hunter type: ")

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
  print("# Display Stats")
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
    print("=================")
    print("# Inventory Menu")
    print("=================")
    print("1. View Inventory")
    print("=================")
    print("2. Use or Drop Item")
    print("=================")
    print("3. Set a Soul Free")
    print("=================")
    print("4. Exit Inventory")
    print("=================")
    choice = input("Choice: ").strip()
    if choice == "1":
      if not Inventory:
        print("Inventory: Empty")
      else:
        for i, it in enumerate(Inventory, 1):
          print(f"{i}. {it}")
    elif choice == "2":
      if not Inventory:
        print("=================")
        print("Inventory empty.")
        print("=================")
        continue
      # show indexed list and allow numeric or name selection
      for i, it in enumerate(Inventory, 1):
        print("=================")
        print(f"{i}. {it}")
        print("=================")
      sel = input("Enter item number or name to use/drop: ").strip()
      print("=================")
      if not sel:
        print("=================")
        print("No selection made.")
        print("=================")
        continue
      # try number
      item = None
      if sel.isdigit():
        idx = int(sel) - 1
        if 0 <= idx < len(Inventory):
          item = Inventory[idx]
        else:
          print("=================")
          print("Invalid item number.")
          print("=================")
          continue
      else:
        # case-insensitive match by name
        lowered = sel.lower()
        for it in Inventory:
          if it.lower() == lowered:
            item = it
            break
        if item is None:
          print("=================")
          print("Item not found.")
          print("=================")
          continue

      # Simple use behavior: potion heals, sword increases strength temporarily, others drop
      if item.lower() == "potion":
        SET_attributes[3] += 20
        print("=================")
        print("You used a Potion. Health increased by 20.")
        print("=================")
      elif item.lower() == "sword":
        SET_attributes[0] += 2
        print("=================")
        print("You equipped a Sword. Strength increased by 2.")
        print("=================")
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
        print("=================")
        print("You set a soul free.")
        print("=================")
      else:
        print("=================")
        print("No souls to free.")
        print("=================")
    elif choice == "4":
      break
    else:
      print("=================")
      print("Invalid choice.")
      print("=================")

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
    print("=================")
    print("# Store Menu ")
    print("=================")
    print(f"Money: {SET_money}")
    print("=================")
    if not SET_store:
      print("=================")
      print("Store is empty.")
      print("=================")
      break
    for item, price in SET_store.items():
      print(f"{item}: {price}")
      print("=================")
    choice = input("Choose an item to buy or type EXIT: ").strip()
    print("=================")
    if not choice:
      print("=================")
      print("Enter a valid item or EXIT.")
      print("=================")
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
      print("=================")
      print("Enter a valid item.")
      print("=================")
      continue
    price = SET_store[chosen_key]
    if price > SET_money:
      print("=================")
      print("Too much for too little money.")
      print("=================")
    else:
      SET_money -= price
      Inventory.append(chosen_key)
      # Remove item from store to match pseudocode's "REMOVE itemChoice from store"
      SET_store.pop(chosen_key, None)
      print("=================")
      print("Item purchased!")
      print("=================")

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
  print("=================")
  print("# Apply Power-Ups")
  print("=================")
  if not SET_powerups:
    print("=================")
    print("No power-ups to apply.")
    print("=================")
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
  print("=================")
  print("# Check Level Up ")
  print("=================")
  leveled = False
  while SET_souls >= 10:
    SET_level += 1
    SET_souls -= 10
    leveled = True
    print("=================")
    print("You leveled up!")
    print("=================")
    if SET_souls >= 10:
      print("=================")
      print("You unlocked a special skill!")
      print("=================")
      SET_skills.append(f"Special Skill L{SET_level}")
      print("=================")
    elif SET_souls >= 5:
      print("=================")
      print("No new skill this level.")
      print("=================")
    else:
      print("=================")
      print("You moved up a level.")
      print("=================")
  if not leveled:
    print("=================")
    print("Not enough souls to level up.")
    print("=================")

#MAIN MENU

#CALL startGame()

#WHILE true
#    DISPLAY "1. View Stats"
#    DISPLAY "2. Inventory"
#    DISPLAY "3. Store"
#    DISPLAY "4. Apply Power-Ups"
#    DISPLAY "5. Exit Game"
#END PROGRAM

while True:
  main()
